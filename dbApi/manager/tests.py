from .models import Dx, Lab, Med, Px, Fx, Event

def total_data(request, case_num: int):
    case_num_string = "Case " + str(case_num)
    events = Event.objects.filter(number=case_num_string)
    dxs = Dx.objects.filter(number=case_num_string)
    labs = Lab.objects.filter(number=case_num_string)
    meds = Med.objects.filter(number=case_num_string)
    fxs = Fx.objects.filter(number=case_num_string)
    pxs = Px.objects.filter(number=case_num_string)

    result_dict = {
        'caseNum' : case_num_string,
        'gender' : labs[0].sex,
        'birthDate': labs[0].birth,
        'events': {},
        'event_dates': []
    }
    prev_date = events[0].date
    for event in events:
        date = event.date
        result_dict['event_dates'].append(date)

        separate_dict = {'dx': [], 'lab': [], 'med': [], 'firsts': [], 'afters': []}

        filtered_dxs = dxs.filter(date=date)
        for dx in filtered_dxs:
            dx_dict = {
                'first_date': dx.first_date,
                'diag_code': dx.diagnostic_code,
                'diag_name': dx.diagnostic_name,
                'ICD10_code': dx.icd10_code

            }
            separate_dict['dx'].append(dx_dict)

        if prev_date == date:
            filtered_labs = labs.filter(date=date)
        else:
            filtered_labs = labs.filter(date__lte=date, date__gt=prev_date)
        for lab in filtered_labs:
            lab_type = "Text"
            if lab.result_numerical:
                lab_type = "Number"
            elif lab.result_negpos:
                lab_type = "NegPos"
            lab_dict = {
                'lab_name': lab.test_name,
                'lab_type': lab_type,
                'lab_num': lab.result_numerical,
                'lab_pn': lab.result_negpos,
                'lab_text': lab.result_total

            }
            separate_dict['lab'].append(lab_dict)

        filtered_meds = meds.filter(date=date)
        for med in filtered_meds:
            med_dict = {
                'med_name_ingr': med.name_ingredient,
                'name_normal': med.name_normal,
                'prescrpition': med.prescription
            }
            separate_dict['med'].append(med_dict)

        filtered_fxs = fxs.filter(date=date)
        for fx in filtered_fxs:
            separate_dict['afters'].append(fx.format_content)

        filtered_pxs = pxs.filter(date=date)
        for px in filtered_pxs:
            separate_dict['firsts'].append(px.format_content)

        prev_date = date
        result_dict['events'][date] = separate_dict

    print(result_dict)

total_data(None, 2)