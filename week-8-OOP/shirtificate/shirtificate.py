# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    shirtificate.py                                   #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/8/shirtificate/

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.ln(25)
        self.set_font("helvetica", "", 50)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        self.image("shirtificate.png", x=10, y=70, w=190)


def main():
    name = input("Name: ").strip()

    pdf = PDF()
    pdf.add_page()

    pdf.set_font("helvetica", "", 25)
    pdf.set_text_color(255, 255, 255)

    pdf.set_x(55)

    pdf.cell(0, 210, f"{name} took CS50")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
