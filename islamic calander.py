from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
import hijri_converter

cal = Calendar()

# Define the content of the ICS file as a string
ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Your Organization//Islamic Calendar Ultimate//EN
X-WR-CALNAME:Islamic Calendar Ultimate
BEGIN:VEVENT
SUMMARY:Example Event
DTSTART:20240224T080000Z
DTEND:20240224T090000Z
END:VEVENT
END:VCALENDAR
"""

# Write the content to an ICS file
with open("islamic_calendar.ics", "w") as file:
    file.write(ics_content)


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
    '1 Muharram': 'Islamic New Year',
    '10 Muharram': 'Shahadat Imam Hussain (A.S.)',
    '20 Muharram': 'Wafaat Janabe Sakina Binte Imam Hussain (A.S.)',
    '25 Muharram': 'Shahadat Imam Zain-ul-Abideen (A.S.)',
    '7 Safar': 'Viladat Imam Musa Kazim (A.S.)',
    '17 Safar': 'Shahadat Imam Ali Reza (A.S.)',
    '20 Safar': 'Chehalum Imam Hussain (A.S.)',
    '24 Safar (or 16 Zilhaj)': 'Shahadat Janabe Zainab',
    '28 Safar': 'Shahadat Imam Hassan (A.S.)',
    '8 Rabi-ul-Awwal': 'Shahadat Imam Hassan Askari (A.S.)',
    '9 Rabi-ul-Awwal': 'Ide Nahum',
    '12 Rabi-ul-Awwal': 'Viladat Holy Prophet (S.A.W.S)',
    '17 Rabi-ul-Awwal': 'Viladat Imam Jafar-e-Sadiq (A.S.)',
    '10 Rabi al-Thani': 'Viladat Imam Hassan Askari (A.S.)',
    '15 Jamadi-ul-Awwal': 'Viladat Imam Zain-ul-Abideen (A.S.)',
    '3 Jumada al-Thani': 'Wafaat Janabe Fatima Zehra (S.A.)',
    '20 Jumada al-Thani': 'Viladat Janabe Fatima Zehra (S.A.)',
    '1 Rajab': 'Viladat Imam Mohammed Baqir (A.S.) & Janabe Sakina Binte Imam Husain (A.S.)',
    '3 Rajab': 'Shahadat Imam Ali Naqi (A.S.)',
    '10 Rajab': 'Viladat Imam Mohammed Taqi 24(A.S.)',
    '13 Rajab': 'Viladat Amirul Momineen Ali (A.S.)',
    '25 Rajab': 'Shahadat Imam Musa Kazim (A.S.)',
    '27 Rajab': 'Al Isra’ wal Mi’raj (The night journey and ascension)',
    '1 Shaban': 'Viladat Janabe Zainab (A.S.)',
    '3 Shaban': 'Viladat Imam Hussain (A.S.)',
    '4 Shaban': 'Viladat Hazrat Abbas ibne Amirul Momineen Ali (A.S.)',
    '11 Shaban': 'Viladat Hazrat Ali Akbar ibne Imam Hussain (A.S.)',
    '15 Shaban': 'Viladat Imam Mehdi Sahebuzzaman (A.S.)',
    '15 Shaban': 'Shab-e-Barat',
    '1 Ramadan': 'Ramadan begins',
    '8 Ramadan': 'Shahadat Hazrat Abu Talib (A.S.)',
    '10 Ramadan': 'Wafaat Hazrat Khadija-tul-Kubra (S.A.)',
    '15 Ramadan': 'Viladat Imam Hassan (A.S.)',
    '18 Ramadan': 'Shab-e-Zarbat Amirul Momineen Ali (A.S.)',
    '21 Ramadan': 'Shahadat Amirul Momineen Ali (A.S.)',
    '19,21,23,25,27 Ramadan': 'Shab-e-Qadar (Revelation of Quran)',
    '1 Shawwal': 'Eid al Fitr',
    '8 Shawwal': 'Janat-ul-Baqi Day',
    '15 Shawwal': 'Shahadat Imam Jafare Sadiq (A.S.)',
    '1 Zeeqadh': 'Wafaat Janabe Fatima Binte Asad',
    '11 Zeeqadh': 'Viladat Imam Ali Reza (A.S.)',
    '29 Zeeqadh': 'Shahadat Imam Mohammed Taqi (A.S.)',
    '1 Dhu al-Hijja': 'Dhu al-Hijja begins',
    '1 Dhu al-Hijja': 'Marriage of Hazrat Fatima Zehra (S.A.) & Hazrat Ali (A.S.)',
    '7 Dhu al-Hijja': 'Shahadat Imam Mohammed Baqir (A.S.)',
    '8 Dhu al-Hijja': 'Hajj begins',
    '9 Dhu al-Hijja': 'Day of ‘Arafah',
    '9 Dhu al-Hijja': 'Shahadat Muslim Ibne Aqil (A.S.)',
    '10 Dhu al-Hijja': 'Eid al Adha',
    '15 Dhu al-Hijja': 'Viladat Imam Ali Naqi (A.S.)',
    '16 Dhu al-Hijja (or 24 Safar)': 'Shahadat Janabe Zainab (A.S.)',
    '18 Dhu al-Hijja': 'Ide Ghadir',
    '22 Dhu al-Hijja': 'Shahadat Tiflaan-e Hazrat Muslim (A.S.)',
    '24 Dhu al-Hijja': 'Ide Mubahela'
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
        event.add('summary', event_name)
        event.add('dtstart', gregorian_date)
        event.add('dtend', gregorian_date)

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
with open('islamic_calendar_2024.ics', 'wb') as f:
    f.write(cal.to_ical())
