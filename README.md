# Projekt-2
Matsvinnssparningen
♻️ Projekt 1: MatsvinnSparningen – Smart Food Waste Dashboard ♻️
✅ Beskrivning 🚯
Systemet övervakar hur många elever som käkar i matsalen varje dag och sparar det i en databas där den även sparar mängden mat som slängts, dagens maträtt och datum. Därefter analyseras datan av en AI som tar reda på hur många som käkat och räknar ut portioner samt matsvinn per elev. Därefter justerar den mängden mat som behövdes beställa och informerar skolan om det.  
✅ Syfte
Skapa ett system som kan hjälpa matleverantören och skolan att beställa in en korrekt mängd mat och undvika matsvinn
✅ Så går eleverna till väga
Planering:
Rita strukturdiagram för träningen av AI, hur räkningen av eleverna ska fungera, frontend, backend.


Datainsamling:
Viktsensor under tallrikarna/kamera över tallrikarna och möjligtvis hitta ett dataset från hur mycket mat som slängts.
Ai träning:
Träna en modell med TensorFlow eller Teachable Machine.


Analys:
Uträkning utav matsvinn per elev (MPE), Hur många elever som åt mat och hur många som inte åt.
 Implementation: 
Kör modellen på en Raspberry Pi eller dator med Python:


Pitch:
Visa systemet live och redovisa matsvinns sparnings systemet
🎯 Globala mål: 12 – Hållbar konsumtion och produktion, 13 – Bekämpa klimatförändringarna.


```mermaid
flowchart TD
    Main["Dashboard"] --> Frontend["Frontend<br>Python GUI"] & Backend["Backend<br>Python"]
    Frontend --> Dashboard["Dashboard"]
    Dashboard --> DropdownMenu["DropdownMenu"]
    DropdownMenu --> Dropdown1["Dropdown att välja Datum"] & Dropdown2["Dropdown För att kolla senste veckan, månaden, År"]
    Dropdown1 --> data2["data: <br>Datum<br>Matsvinn(KG)<br>Antal Elever som ätit mat<br>Maträtt<br>"]
    Dropdown2 --> data3["Matsvinn/ Per Elev ( MPE)<br>Start Datum<br>Slut Datum"]
   
    Backend --> databas["MongoDB"] & AI["AI som läser av elever<br>(Kamera vid ingång och utgång/över talrikar)"]
    databas --> data1["data<br>Datum<br>Matsvinn/KG)<br>Antal Elever<br>Maträtt"]
    AI --> Function["Function<br>Räknar totala Elever"]
    Function --> data1
    data1-->Backend
    Backend-->Frontend
