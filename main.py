import pikepdf
import os
from datetime import datetime


def merge_pdfs_with_outline():
    # 获取当前目录下所有的PDF文件
    pdf_files = [f for f in os.listdir(".") if f.endswith(".pdf")]

    if len(pdf_files) < 2:
        print("当前目录下PDF文件少于2个！")
        return

    try:
        pdf_files.sort()
        output_name = "merged_output.pdf"
        merged_pdf = pikepdf.Pdf.new()
        outline = merged_pdf.open_outline()
        current_page = 0
        for pdf_file in pdf_files:
            print(f"正在处理: {pdf_file}")
            pdf = pikepdf.Pdf.open(pdf_file)
            merged_pdf.pages.extend(pdf.pages)
            if current_page < len(merged_pdf.pages):
                outline.add(
                    title=os.path.splitext(pdf_file)[0].lstrip("0"),
                    destination=merged_pdf.pages[current_page].index,
                )

            current_page += len(pdf.pages)

        merged_pdf.save(output_name)

        print(f"\nPDF文件合并成功！")
        print(f"输出文件：{output_name}")
        print(f"合并的文件：{', '.join(pdf_files)}")

    except Exception as e:
        print(f"合并过程中出现错误：{str(e)}")


if __name__ == "__main__":
    merge_pdfs_with_outline()
