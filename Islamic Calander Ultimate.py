from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
import hijri_converter

cal = Calendar()

# Define the calendar name
calendar_name = 'Islamic Calendar Ultimate'

cal.add('X-WR-CALNAME', calendar_name)  # Add X-WR-CALNAME directly to the calendar

month_mapping = {
    'Muharram': 1,
    'Safar': 2,
    'Rabi-ul-Awwal': 3,
    'Rabi al-Thani': 4,  
    'Jamadi-ul-Awwal': 5,
    'Jumada al-Thani': 6,
    'Rajab': 7,
    'Shaban': 8,
    'Ramadan': 9,
    'Shawwal': 10,
    'Zeeqadh': 11,
    'Dhu al-Hijja': 12
}

events = {
    '1 Muharram': 'Islamic New Year - Description: This day marks the beginning of the month of Muharram in the Islamic calendar.',
    '10 Muharram': 'Martyrdom of Imam Hussain (A.S.) - Description: The martyrdom of Imam Hussain (A.S.), the grandson of Prophet Muhammad (S.A.W.), took place in the year 61 AH in Karbala, Iraq.',
    '20 Muharram': 'Demise of Sakina bint Imam Hussain (A.S.) - Description: The demise of Sakina bint Imam Hussain (A.S.), the beloved daughter of Imam Hussain (A.S.), occurred in the year 61 AH in the prison of Damascus, Syria.',
    '25 Muharram': 'Martyrdom of Imam Ali ibn Hussain Zain-ul-Abideen (A.S.) - Description: Imam Ali ibn Hussain Zain-ul-Abideen (A.S.), the son of Imam Hussain (A.S.) and the great-grandson of Prophet Muhammad (S.A.W.), was martyred in the year 95 AH in Medina, Saudi Arabia.',
    '1 Safar': 'First Day of Safar - Description: This day marks the beginning of the month of Safar in the Islamic calendar.',
    '7 Safar': 'Birth of Imam Musa al-Kazim (A.S.) - Description: Imam Musa al-Kazim (A.S.), the seventh Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was born in the year 128 AH.',
    '17 Safar': 'Martyrdom of Imam Ali ibn Musa al-Reza (A.S.) - Description: Imam Ali ibn Musa al-Reza (A.S.), the eighth Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was martyred in the year 203 AH in Mashhad, Iran.',
    '20 Safar': 'Arbaeen of Imam Hussain (A.S.) - Description: Arbaeen marks the 40th day after the martyrdom of Imam Hussain (A.S.), the grandson of Prophet Muhammad (S.A.W.), in the year 61 AH in Karbala, Iraq.',
    '24 Safar (or 16 Zilhaj)': 'Martyrdom of Zainab bint Ali (A.S.) - Description: Zainab bint Ali (A.S.), the daughter of Imam Ali (A.S.) and the granddaughter of Prophet Muhammad (S.A.W.), is believed to have been martyred in the year 62 AH.',
    '28 Safar': 'Martyrdom of Imam Hassan ibn Ali (A.S.) - Description: Imam Hassan ibn Ali (A.S.), the second Imam of the Shia Muslims and the grandson of Prophet Muhammad (S.A.W.), was martyred in the year 50 AH in Medina, Saudi Arabia.',
    '1 Rabi-ul-Awwal': 'First Day of Rabi-ul-Awwal - Description: This day marks the beginning of the month of Rabi-ul-Awwal in the Islamic calendar.',
    '8 Rabi-ul-Awwal': 'Martyrdom of Imam Hasan al-Askari (A.S.) - Description: Imam Hasan al-Askari (A.S.), the eleventh Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was martyred in the year 260 AH in Samarra, Iraq.',
    '12 Rabi-ul-Awwal': 'Birth of Holy Prophet Muhammad (S.A.W.S) - Description: The birth of Prophet Muhammad (S.A.W.), the final messenger of Islam, is celebrated on this day, believed to be in the year 570 AD in Mecca, Saudi Arabia.',
    '17 Rabi-ul-Awwal': 'Birth of Imam Jafar al-Sadiq (A.S.) - Description: Imam Jafar al-Sadiq (A.S.), the sixth Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was born in the year 83 AH in Medina, Saudi Arabia.',
    '1 Rabi al-Thani': 'First Day of Rabi al-Thani - Description: This day marks the beginning of the month of Rabi-ul-Awwal in the Islamic calendar.',
    '10 Rabi al-Thani': 'Birth of Imam Hasan al-Askari (A.S.) - Description: Imam Hasan al-Askari (A.S.), the eleventh Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was born on this day in the year 232 AH in Medina, Saudi Arabia.',
    '1 Jamadi-ul-Awwal': 'First Day of Jamadi-ul-Awwal - Description: This day marks the beginning of the month of Rabi-ul-Awwal in the Islamic calendar.',
    '15 Jamadi-ul-Awwal': 'Birth of Imam Ali ibn Hussain Zain-ul-Abideen (A.S.) - Description: Imam Ali ibn Hussain Zain-ul-Abideen (A.S.), the fourth Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was born on this day in the year 38 AH in Medina, Saudi Arabia.',
    '1 Jumada al-Thani': 'First Day of Jumada al-Thani- Description: This day marks the beginning of the month of Jumada al-Thani in the Islamic calendar.',
    '3 Jumada al-Thani': 'Demise of Lady Fatima Zahra (S.A.) - Description: Lady Fatima Zahra (S.A.), the daughter of Prophet Muhammad (S.A.W.) and the wife of Imam Ali (A.S.), passed away on this day in the year 11 AH in Medina, Saudi Arabia.',
    '20 Jumada al-Thani': 'Birth of Lady Fatima Zahra (S.A.) - Description: Lady Fatima Zahra (S.A.), the beloved daughter of Prophet Muhammad (S.A.W.) and an esteemed figure in Islam, was born on this day in the year 615 AD in Mecca, Saudi Arabia.',
    '1 Rajab': 'First Day of Rajab - Description: This day marks the beginning of the month of Rajab in the Islamic calendar.',
    '1 Rajab': 'Birth of Imam Muhammad al-Baqir (A.S.) & Lady Sakina bint Imam Hussain (A.S.) - Description: Imam Muhammad al-Baqir (A.S.), the fifth Imam of the Shia Muslims, was born on this day in the year 57 AH in Medina, Saudi Arabia. Lady Sakina, the daughter of Imam Hussain (A.S.), is also commemorated on this day.',
    '3 Rajab': 'Martyrdom of Imam Ali al-Naqi (A.S.) - Description: Imam Ali al-Naqi (A.S.), the tenth Imam of the Shia Muslims, was martyred on this day in the year 254 AH in Samarra, Iraq.',
    '10 Rajab': 'Birth of Imam Muhammad al-Taqi (A.S.) - Description: Imam Muhammad al-Taqi (A.S.), the ninth Imam of the Shia Muslims, was born on this day in the year 195 AH in Medina, Saudi Arabia.',
    '13 Rajab': 'Birth of Commander of the Faithful, Ali ibn Abi Talib (A.S.) - Description: Imam Ali ibn Abi Talib (A.S.), the first Imam of the Shia Muslims and the fourth Caliph of the Sunni Muslims, was born on this day in the year 600 AD in Mecca, Saudi Arabia.',
    '25 Rajab': 'Martyrdom of Imam Musa al-Kazim (A.S.) - Description: Imam Musa al-Kazim (A.S.), the seventh Imam of the Shia Muslims, was martyred on this day in the year 183 AH in Baghdad, Iraq.',
    '27 Rajab': 'Al Isra’ wal Mi’raj (The night journey and ascension) - Description: This event commemorates the night journey and ascension of Prophet Muhammad (S.A.W.) to the heavens, which is believed to have taken place on this day.',
    '1 Shaban': 'First Day of Shaban - Description: This day marks the beginning of the month of Shaban in the Islamic calendar.',
    '1 Shaban': 'Birth of Lady Zainab bint Ali (A.S.) - Description: Lady Zainab bint Ali (A.S.), the daughter of Imam Ali (A.S.) and the granddaughter of Prophet Muhammad (S.A.W.), was born on this day in the year 626 AD in Medina, Saudi Arabia.',
    '3 Shaban': 'Birth of Imam Hussain ibn Ali (A.S.) - Description: Imam Hussain ibn Ali (A.S.), the third Imam of the Shia Muslims and the grandson of Prophet Muhammad (S.A.W.), was born on this day in the year 626 AD in Medina, Saudi Arabia.',
    '4 Shaban': 'Birth of Hazrat Abbas ibn Ali (A.S.) - Description: Hazrat Abbas ibn Ali (A.S.), the son of Imam Ali (A.S.) and the brother of Imam Hussain (A.S.), was born on this day in the year 647 AD in Medina, Saudi Arabia.',
    '11 Shaban': 'Birth of Hazrat Ali Akbar ibn Hussain (A.S.) - Description: Hazrat Ali Akbar ibn Hussain (A.S.), the son of Imam Hussain (A.S.), was born on this day. He is remembered for his bravery and resemblance to his grandfather, Prophet Muhammad (S.A.W.).',
    '15 Shaban': 'Birth of Imam Mahdi (A.S.) - Description: Imam Mahdi (A.S.), the twelfth and final Imam of the Shia Muslims, was born on this day in the year 255 AH in Samarra, Iraq. This day is also observed as Shab-e-Barat, a night of forgiveness and prayers in Islamic tradition.',
    '1 Ramadan': 'Ramadan begins - Description: This day marks the beginning of the month of Ramadan in the Islamic calendar.',
    '8 Ramadan': 'Martyrdom of Hazrat Abu Talib (A.S.) - Description: Hazrat Abu Talib (A.S.), the uncle and protector of Prophet Muhammad (S.A.W.), passed away on this day in the year 619 AD in Mecca, Saudi Arabia.',
    '10 Ramadan': 'Demise of Hazrat Khadija-tul-Kubra (S.A.) - Description: Hazrat Khadija-tul-Kubra (S.A.), the first wife of Prophet Muhammad (S.A.W.) and the mother of the believers, passed away on this day in the year 619 AD in Mecca, Saudi Arabia.',
    '15 Ramadan': 'Birth of Imam Hassan ibn Ali (A.S.) - Description: Imam Hassan ibn Ali (A.S.), the second Imam of the Shia Muslims and the grandson of Prophet Muhammad (S.A.W.), was born on this day in the year 625 AD in Medina, Saudi Arabia.',
    '17 Ramadan': 'Demise of Sayyidah Aisha bint Abi Bakr (RA) - Description: Sayyidah Aisha bint Abi Bakr (RA), the wife of Prophet Muhammad (S.A.W.) and a prominent figure in Islamic history, passed away on this day in the year 678 AD in Medina, Saudi Arabia.',
    '18 Ramadan': 'Night of the Strike of Commander of the Faithful, Ali (A.S.) - Description: On this night, Imam Ali ibn Abi Talib (A.S.), the first Imam of the Shia Muslims and the fourth Caliph of the Sunni Muslims, was struck by a poisoned sword while praying in the mosque of Kufa, Iraq.',
    '21 Ramadan': 'Martyrdom of Commander of the Faithful, Ali (A.S.) - Description: Imam Ali ibn Abi Talib (A.S.) succumbed to his injuries and was martyred on this day in the year 661 AD in Kufa, Iraq.',
    '19 Ramadan': 'Nights of Qadr (Revelation of Quran) - Description: These nights are observed as the Nights of Qadr, during which the Quran was revealed to Prophet Muhammad (S.A.W.). They are considered the holiest nights in the Islamic calendar.',
    '21 Ramadan': 'Nights of Qadr (Revelation of Quran) - Description: These nights are observed as the Nights of Qadr, during which the Quran was revealed to Prophet Muhammad (S.A.W.). They are considered the holiest nights in the Islamic calendar.',
    '23 Ramadan': 'Nights of Qadr (Revelation of Quran) - Description: These nights are observed as the Nights of Qadr, during which the Quran was revealed to Prophet Muhammad (S.A.W.). They are considered the holiest nights in the Islamic calendar.',
    '25 Ramadan': 'Nights of Qadr (Revelation of Quran) - Description: These nights are observed as the Nights of Qadr, during which the Quran was revealed to Prophet Muhammad (S.A.W.). They are considered the holiest nights in the Islamic calendar.',
    '27 Ramadan': 'Nights of Qadr (Revelation of Quran) - Description: These nights are observed as the Nights of Qadr, during which the Quran was revealed to Prophet Muhammad (S.A.W.). They are considered the holiest nights in the Islamic calendar.',
    '1 Shawwal': 'Eid al-Fitr - Description: Eid al-Fitr is the festival celebrated by Muslims worldwide to mark the end of the month of Ramadan and the beginning of Shawwal.',
    '15 Shawwal': 'Martyrdom of Imam Jafar al-Sadiq (A.S.) - Description: Imam Jafar al-Sadiq (A.S.), the sixth Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was martyred on this day in the year 148 AH in Medina, Saudi Arabia.',
    '1 Zeeqadh': 'First Day of Zeeqadh - Description: This day marks the beginning of the month of Zeeqadh in the Islamic calendar.',
    '1 Zeeqadh': 'Demise of Lady Fatima bint Asad - Description: Lady Fatima bint Asad, the mother of Imam Ali (A.S.) and a respected figure in Islamic history, passed away on this day in Medina, Saudi Arabia.',
    '11 Zeeqadh': 'Birth of Imam Ali ibn Musa al-Reza (A.S.) - Description: Imam Ali ibn Musa al-Reza (A.S.), the eighth Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was born on this day in the year 148 AH in Medina, Saudi Arabia.',
    '29 Zeeqadh': 'Martyrdom of Imam Muhammad al-Taqi (A.S.) - Description: Imam Muhammad al-Taqi (A.S.), the ninth Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was martyred on this day in the year 220 AH in Baghdad, Iraq.',
    '1 Dhu al-Hijja': 'Dhu al-Hijja begins - Description: This day marks the beginning of the month of Dhu al-Hijja in the Islamic calendar.',
    '1 Dhu al-Hijja': 'Marriage of Lady Fatima Zahra (S.A.) & Commander of the Faithful, Ali (A.S.) - Description: The marriage of Lady Fatima Zahra (S.A.), the daughter of Prophet Muhammad (S.A.W.), and Imam Ali ibn Abi Talib (A.S.), the first Imam of the Shia Muslims, took place on this day.',
    '7 Dhu al-Hijja': 'Martyrdom of Imam Muhammad al-Baqir (A.S.) - Description: Imam Muhammad al-Baqir (A.S.), the fifth Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was martyred on this day in the year 114 AH in Medina, Saudi Arabia.',
    '8 Dhu al-Hijja': 'Hajj begins - Description: The annual pilgrimage of Hajj, one of the five pillars of Islam, begins on this day in Mecca, Saudi Arabia.',
    '9 Dhu al-Hijja': 'Day of ‘Arafah - Description: The Day of ‘Arafah is considered one of the most important and sacred days in the Islamic calendar, observed during the Hajj pilgrimage.',
    '9 Dhu al-Hijja': 'Martyrdom of Muslim ibn Aqil (A.S.) - Description: Muslim ibn Aqil (A.S.), the cousin and emissary of Imam Hussain (A.S.), was martyred on this day in the year 60 AH in Kufa, Iraq.',
    '10 Dhu al-Hijja': 'Eid al-Adha - Description: Eid al-Adha, also known as the Festival of Sacrifice, is celebrated by Muslims worldwide on this day, commemorating the willingness of Prophet Ibrahim (A.S.) to sacrifice his son as an act of obedience to God.',
    '15 Dhu al-Hijja': 'Birth of Imam Ali al-Naqi (A.S.) - Description: Imam Ali al-Naqi (A.S.), the tenth Imam of the Shia Muslims and a descendant of Prophet Muhammad (S.A.W.), was born on this day in the year 212 AH in Medina, Saudi Arabia.',
    '16 Dhu al-Hijja (or 24 Safar)': 'Martyrdom of Lady Zainab bint Ali (A.S.) - Description: Lady Zainab bint Ali (A.S.), the daughter of Imam Ali (A.S.) and the granddaughter of Prophet Muhammad (S.A.W.), is believed to have been martyred on this day.',
    '18 Dhu al-Hijja': 'Eid al-Ghadir - Description: Eid al-Ghadir is celebrated by Shia Muslims to commemorate the event of Ghadir Khumm, where Prophet Muhammad (S.A.W.) declared Imam Ali (A.S.) as his successor.',
    '22 Dhu al-Hijja': 'Martyrdom of the Children of Hazrat Muslim ibn Aqil (A.S.) - Description: The children of Hazrat Muslim ibn Aqil (A.S.), who were martyred in the aftermath of their father’s death, are remembered on this day.',
    '24 Dhu al-Hijja': 'Eid al-Mubahela - Description: Eid al-Mubahela commemorates the event of Mubahela, a public debate and invocation for divine curse to reveal the truth, which took place between Prophet Muhammad (S.A.W.) and a Christian delegation from Najran.'
}

for islamic_date, event_name in events.items():
    parts = islamic_date.split()
    days = parts[0].split(',')  
    if parts[1] in ['Rabi', 'Jumada', 'Dhu']:
        month_name = ' '.join(parts[1:3]) 
    else:
        month_name = parts[1]

    month = month_mapping[month_name]

    for day in days:
        # Convert Hijri to Gregorian
        gregorian_date = hijri_converter.convert.Hijri(1445, month, int(day)).to_gregorian()   

       # Create an event
        event = Event()
        summary_description = event_name.split(' - ', 1)  # Split only once
        event.add('summary', islamic_date + ' - ' + summary_description[0])
        description_text = summary_description[1] if len(summary_description) > 1 else ''
        event.add('description', description_text.replace('Description: ', ''))  # Remove "Description:" from the text

        # Add 24-hour reminder
        alarm_24hr = Alarm()
        alarm_24hr.add('action', 'DISPLAY')
        alarm_24hr.add('description', 'Reminder: ' + event_name)
        alarm_24hr.add('trigger', timedelta(hours=-24))
        event.add_component(alarm_24hr)

        # Add 12-hour reminder
        alarm_12hr = Alarm()
        alarm_12hr.add('action', 'DISPLAY')
        alarm_12hr.add('description', 'Reminder: ' + event_name)
        alarm_12hr.add('trigger', timedelta(hours=-12))
        event.add_component(alarm_12hr)



        cal.add_component(event)

# Write the calendar to a file
with open('islamic_calendar_ultimate.ics', 'wb') as f:
    f.write(cal.to_ical())
