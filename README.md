# Projekt-2
Matsvinnssparningen

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
