from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.urls import reverse
from .models import Student
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO

# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4

def student_curd(request):
    if request.method == "POST":
        data = StudentForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect(reverse('student_table'))
    else:
        data = StudentForm()
    return render(request, 'student_curd.html',{'data':data})


def student_table(request):
    students = Student.objects.all()
    return render(request,'student.html',{'students':students})


def student_delete(request,roll_number):
    print(roll_number)
    students = Student.objects.get(roll_number=roll_number)
    students.delete()
    return redirect(reverse('student_table'))


def student_edit(request,roll_number):
    students = Student.objects.get(roll_number=roll_number)
    if request.method == "POST":
        data = StudentForm(request.POST,instance=students)
        if data.is_valid():
            data.save()
            return redirect(reverse('student_table'))
    else:
        data = StudentForm(instance=students)
    return render(request,'student_update.html',{'data':data})

def renader_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def student_download(request, roll_number):
    # print(roll_number)
    student = Student.objects.get(roll_number=roll_number)

    data = {
        'student':student,
    }

    pdf = renader_to_pdf('student_report.html', data)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="students_report.pdf"'
        return response

    # w, h = A4
    # c = canvas.Canvas("static/uploads/students_report.pdf", pagesize=A4)

    # c.drawString(200, 750, "Student Report")
    # c.drawString(200, 730, "Roll Number: " + str(row.roll_number))
    # c.drawString(200, 710, "First Name: " + row.first_name)
    # c.drawString(200, 690, "Last Name: " + row.last_name)
    # c.drawString(200, 670, "Email: " + row.email)
    # c.drawString(200, 650, "Phone Number: " + str(row.phone_number))
    # c.drawString(200, 630, "Address: " + row.address)

    # c.showPage()
    # c.save()


   

    return HttpResponse("Not Found")