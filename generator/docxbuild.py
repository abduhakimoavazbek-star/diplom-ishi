# -*- coding: utf-8 -*-
"""
Toza Python (stdlib) bilan .docx (OOXML) hujjat yaratuvchi minimal kutubxona.
python-docx talab qilmaydi. Sarlavhalar, paragraflar, jadvallar, rasmlar,
sahifa uzilishi va A4 sahifa sozlamalarini qo'llab-quvvatlaydi.
"""
import os
import zipfile
from xml.sax.saxutils import escape

EMU_PER_PX = 9525  # 96 dpi


def _esc(t):
    return escape(str(t))


class Docx:
    def __init__(self):
        self.body = []          # XML bo'laklari ro'yxati
        self.images = []        # (rId, arc_name, src_path)
        self._img_counter = 0

    # ---- matn yugurtgichlari (runs) ----
    @staticmethod
    def _run(text, bold=False, italic=False, size=None, color=None, sub=False, sup=False):
        rpr = []
        if bold:
            rpr.append("<w:b/>")
        if italic:
            rpr.append("<w:i/>")
        if size:
            rpr.append(f'<w:sz w:val="{size*2}"/><w:szCs w:val="{size*2}"/>')
        if color:
            rpr.append(f'<w:color w:val="{color}"/>')
        if sub:
            rpr.append('<w:vertAlign w:val="subscript"/>')
        if sup:
            rpr.append('<w:vertAlign w:val="superscript"/>')
        rpr_xml = f"<w:rPr>{''.join(rpr)}</w:rPr>" if rpr else ""
        return f'<w:r>{rpr_xml}<w:t xml:space="preserve">{_esc(text)}</w:t></w:r>'

    # ---- paragraf ----
    def para(self, text="", style=None, align=None, bold=False, italic=False,
             size=None, runs=None, spacing_after=120, indent=None, color=None):
        ppr = []
        if style:
            ppr.append(f'<w:pStyle w:val="{style}"/>')
        if align:
            ppr.append(f'<w:jc w:val="{align}"/>')
        if indent:
            ppr.append(f'<w:ind w:firstLine="{indent}"/>')
        ppr.append(f'<w:spacing w:after="{spacing_after}" w:line="276" w:lineRule="auto"/>')
        ppr_xml = f"<w:pPr>{''.join(ppr)}</w:pPr>"
        if runs is None:
            runs_xml = self._run(text, bold=bold, italic=italic, size=size, color=color) if text else ""
        else:
            runs_xml = "".join(runs)
        self.body.append(f"<w:p>{ppr_xml}{runs_xml}</w:p>")

    def heading(self, text, level=1, numbered=True):
        style = f"Heading{level}"
        self.body.append(
            f'<w:p><w:pPr><w:pStyle w:val="{style}"/>'
            f'<w:keepNext/><w:spacing w:before="240" w:after="120"/></w:pPr>'
            f'{self._run(text, bold=True)}</w:p>'
        )

    def title(self, text, size=28, align="center", spacing_after=240):
        self.body.append(
            f'<w:p><w:pPr><w:jc w:val="{align}"/>'
            f'<w:spacing w:after="{spacing_after}"/></w:pPr>'
            f'{self._run(text, bold=True, size=size)}</w:p>'
        )

    def page_break(self):
        self.body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def formula(self, text, label=None):
        """Markazlashtirilgan formula (kursiv)."""
        runs = [self._run(text, italic=True, size=13)]
        if label:
            runs.append(self._run("        (" + label + ")", size=11))
        self.body.append(
            f'<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="60" w:after="60"/></w:pPr>'
            f'{"".join(runs)}</w:p>'
        )

    def bullet(self, text):
        self.body.append(
            f'<w:p><w:pPr><w:pStyle w:val="ListBullet"/>'
            f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
            f'<w:spacing w:after="60"/></w:pPr>{self._run(text)}</w:p>'
        )

    def numbered(self, text):
        self.body.append(
            f'<w:p><w:pPr>'
            f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>'
            f'<w:spacing w:after="60"/></w:pPr>{self._run(text)}</w:p>'
        )

    # ---- jadval ----
    def table(self, rows, header=True, caption=None, widths=None, font_size=11):
        """rows: qatorlar ro'yxati, har biri kataklar ro'yxati (matn)."""
        ncol = max(len(r) for r in rows)
        if widths is None:
            total = 9300
            widths = [total // ncol] * ncol
        grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
        trs = []
        for ri, row in enumerate(rows):
            cells = []
            is_head = header and ri == 0
            shd = '<w:shd w:val="clear" w:color="auto" w:fill="D9E2F3"/>' if is_head else ""
            for ci in range(ncol):
                txt = row[ci] if ci < len(row) else ""
                tcpr = (f'<w:tcPr><w:tcW w:w="{widths[ci]}" w:type="dxa"/>{shd}'
                        f'<w:vAlign w:val="center"/></w:tcPr>')
                run = self._run(txt, bold=is_head, size=font_size)
                jc = '<w:jc w:val="center"/>' if is_head else ""
                cells.append(
                    f'<w:tc>{tcpr}<w:p><w:pPr>{jc}'
                    f'<w:spacing w:after="20" w:line="240" w:lineRule="auto"/></w:pPr>{run}</w:p></w:tc>'
                )
            trs.append(f"<w:tr>{'<w:trPr><w:tblHeader/></w:trPr>' if is_head else ''}{''.join(cells)}</w:tr>")
        borders = ("<w:tblBorders>"
                   '<w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                   '<w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                   '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                   '<w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                   '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                   '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                   "</w:tblBorders>")
        tbl = (f'<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/>'
               f'<w:jc w:val="center"/>{borders}</w:tblPr>'
               f'<w:tblGrid>{grid}</w:tblGrid>{"".join(trs)}</w:tbl>'
               f'<w:p><w:pPr><w:spacing w:after="0"/></w:pPr></w:p>')
        self.body.append(tbl)
        if caption:
            self.body.append(
                f'<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="40" w:after="160"/></w:pPr>'
                f'{self._run(caption, italic=True, size=10)}</w:p>'
            )

    # ---- rasm ----
    def image(self, src_path, width_px=560, caption=None):
        from struct import unpack
        # PNG o'lchamlarini o'qish
        with open(src_path, "rb") as f:
            data = f.read(24)
        w, h = unpack(">II", data[16:24])
        ratio = h / w
        disp_w = width_px
        disp_h = int(width_px * ratio)
        emu_w = disp_w * EMU_PER_PX
        emu_h = disp_h * EMU_PER_PX
        self._img_counter += 1
        rid = f"rIdImg{self._img_counter}"
        arc = f"media/image{self._img_counter}.png"
        self.images.append((rid, arc, src_path))
        docpr_id = 100 + self._img_counter
        drawing = (
            '<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="80" w:after="40"/></w:pPr>'
            '<w:r><w:drawing>'
            f'<wp:inline distT="0" distB="0" distL="0" distR="0">'
            f'<wp:extent cx="{emu_w}" cy="{emu_h}"/>'
            '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
            f'<wp:docPr id="{docpr_id}" name="Picture {docpr_id}"/>'
            '<wp:cNvGraphicFramePr><a:graphicFrameLocks '
            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>'
            '</wp:cNvGraphicFramePr>'
            '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
            '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:nvPicPr><pic:cNvPr id="{docpr_id}" name="img{self._img_counter}.png"/>'
            '<pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            '<pic:spPr><a:xfrm><a:off x="0" y="0"/>'
            f'<a:ext cx="{emu_w}" cy="{emu_h}"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
            '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
        )
        self.body.append(drawing)
        if caption:
            self.body.append(
                f'<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="160"/></w:pPr>'
                f'{self._run(caption, italic=True, size=10)}</w:p>'
            )

    # ---- saqlash ----
    def save(self, path):
        document = self._document_xml()
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("[Content_Types].xml", self._content_types())
            z.writestr("_rels/.rels", self._root_rels())
            z.writestr("word/document.xml", document)
            z.writestr("word/styles.xml", self._styles())
            z.writestr("word/numbering.xml", self._numbering())
            z.writestr("word/_rels/document.xml.rels", self._doc_rels())
            for rid, arc, src in self.images:
                z.write(src, "word/" + arc)

    def _document_xml(self):
        sect = (
            '<w:sectPr>'
            '<w:pgSz w:w="11906" w:h="16838"/>'
            '<w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1701" '
            'w:header="708" w:footer="708" w:gutter="0"/>'
            '<w:pgNumType w:start="1"/>'
            '</w:sectPr>'
        )
        ns = (
            'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
            'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"'
        )
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<w:document {ns}><w:body>{"".join(self.body)}{sect}</w:body></w:document>'
        )

    def _content_types(self):
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Default Extension="png" ContentType="image/png"/>'
            '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
            '<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>'
            '</Types>'
        )

    def _root_rels(self):
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            '</Relationships>'
        )

    def _doc_rels(self):
        rels = [
            '<Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>',
            '<Relationship Id="rIdNum" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>',
        ]
        for rid, arc, src in self.images:
            rels.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{arc}"/>')
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            + "".join(rels) + '</Relationships>'
        )

    def _styles(self):
        def hstyle(idx, size, before):
            return (
                f'<w:style w:type="paragraph" w:styleId="Heading{idx}"><w:name w:val="heading {idx}"/>'
                f'<w:basedOn w:val="Normal"/><w:next w:val="Normal"/>'
                f'<w:pPr><w:keepNext/><w:spacing w:before="{before}" w:after="120"/>'
                f'<w:outlineLvl w:val="{idx-1}"/></w:pPr>'
                f'<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>'
                f'<w:b/><w:sz w:val="{size*2}"/><w:szCs w:val="{size*2}"/></w:rPr></w:style>'
            )
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            '<w:docDefaults><w:rPrDefault><w:rPr>'
            '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
            '<w:sz w:val="28"/><w:szCs w:val="28"/><w:lang w:val="en-US"/>'
            '</w:rPr></w:rPrDefault></w:docDefaults>'
            '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/>'
            '<w:pPr><w:jc w:val="both"/></w:pPr>'
            '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="28"/></w:rPr></w:style>'
            + hstyle(1, 15, 280) + hstyle(2, 14, 220) + hstyle(3, 13, 180)
            + '<w:style w:type="paragraph" w:styleId="ListBullet"><w:name w:val="List Bullet"/>'
              '<w:basedOn w:val="Normal"/></w:style>'
            '</w:styles>'
        )

    def _numbering(self):
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            '<w:abstractNum w:abstractNumId="0"><w:lvl w:ilvl="0"><w:start w:val="1"/>'
            '<w:numFmt w:val="bullet"/><w:lvlText w:val="&#8211;"/><w:lvlJc w:val="left"/>'
            '<w:pPr><w:ind w:left="567" w:hanging="283"/></w:pPr></w:lvl></w:abstractNum>'
            '<w:abstractNum w:abstractNumId="1"><w:lvl w:ilvl="0"><w:start w:val="1"/>'
            '<w:numFmt w:val="decimal"/><w:lvlText w:val="%1."/><w:lvlJc w:val="left"/>'
            '<w:pPr><w:ind w:left="567" w:hanging="360"/></w:pPr></w:lvl></w:abstractNum>'
            '<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>'
            '<w:num w:numId="2"><w:abstractNumId w:val="1"/></w:num>'
            '</w:numbering>'
        )
