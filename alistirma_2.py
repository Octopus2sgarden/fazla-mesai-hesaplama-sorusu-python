work_hours = input('Saat bilgisi giriniz: ')
hourly_wage = input('Saaatlik ücret bilgisi giriniz:')
h_w = int(hourly_wage)
w_h = int(work_hours)
if w_h < 40:
    total_wage = w_h * h_w 
    print(f"Ödenecek tutar: {total_wage}") 
else:
    total_wage = (w_h - 40) * h_w * 1.5 + 40 * h_w 
    print(f"Ödenecek tutar: {total_wage}")  