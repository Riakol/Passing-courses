first_date = min(florida_hurricane_dates)

iso = 'Дата первого урагана в ISO формате: ' + first_date.strftime('%Y-%m-%d')
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

print(iso)
print(ru)
print(us)
