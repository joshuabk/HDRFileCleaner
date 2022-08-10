from django.shortcuts import render, redirect

import pydicom as pyd


# Create your views here.

def Import(request):
    print(request.method)
    if request.method  == 'POST':
        #form = SaveFileForm(request.POST, request.FILES)
        dcmFile = request.FILES['dicomFile']
        plan = pyd.dcmread( dcmFile )
        plan.SourceSequence[0].SourceIsotopeName = "GammaMed Plus HDR source 0.9mm" 
        PtName = str(plan.PatientName)
        PtName = PtName[:-3]
        PtName = PtName.replace('^',', ')
        pyd.dcmwrite("P:\\Outpatient Oncology\\DOSIMETRY - PHYSICS\Brachytherapy\\NSH HDR\Modified Dicom Files\\"+PtName+".dcm", plan)
       

        return redirect('/Hello' )
    else:
        print("this worked")
        return render(request, 'Import.html', {})
   
def Hello(request):

    return render(request, 'hello.html', {})