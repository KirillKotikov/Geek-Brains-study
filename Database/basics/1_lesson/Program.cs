
Random random = new Random();
string[] sexes = {"мужской", "женский"};
// bus
string busColumns = "bus_id;manufacturer;model;production_year;passengers_count;\n";
int busCount = 10;

for (int id = 1; id <= busCount; id++)
{
    string[] manufacturers = {"Mercedes", "Kamaz", "Man"};
    string manufacturer = manufacturers[random.Next(manufacturers.Length)];
    string model = $"Модель_{random.Next(1, 10)}";
    int productionYear = random.Next(1980, 2022);
    int passengersCount = random.Next(30, 45);

    busColumns += $"{id};{manufacturer};{model};{productionYear};{passengersCount};\n";
}
File.WriteAllText("buses.csv", busColumns);

// driver
string driverColumns = "driver_id;first_name;last_name;birthday;sex;\n";
int driverCount = 10;

for (int id = 1; id <= driverCount; id++)
{
    string firstName = $"Имя_{id}";
    string lastName = $"Фамилия_{id}";
    string sex = sexes[random.Next(sexes.Length)];

    int day = random.Next(1, 28);
    int month = random.Next(1, 13);
    int year = random.Next(1960, 2004);
    string birthday = day + "." + month + "." + year;

    driverColumns += $"{id};{firstName};{lastName};{birthday};{sex};\n";
}
File.WriteAllText("drivers.csv", driverColumns);

// conductor
string conductorColumns = "conductor_id;first_name;last_name;birthday;sex;\n";
int conductorCount = 10;

for (int id = 1; id <= conductorCount; id++)
{
    string firstName = $"Имя_{id}";
    string lastName = $"Фамилия_{id}";
    string sex = sexes[random.Next(sexes.Length)];

    int day = random.Next(1, 28);
    int month = random.Next(1, 13);
    int year = random.Next(1960, 2004);
    string birthday = day + "." + month + "." + year;

    conductorColumns += $"{id};{firstName};{lastName};{birthday};{sex};\n";
}
File.WriteAllText("conductors.csv", conductorColumns);

// trip
string tripColumns = "trip_id;trip_name;bus_id;driver_id;conductor_id;\n";
int tripCount = 10;

for (int id = 1; id <= tripCount; id++)
{
    string tripName = $"Имя_{id}";
    int busId = random.Next(1, busCount);
    int driverId = random.Next(1, driverCount);
    int conductorId = random.Next(1, conductorCount);
    
    tripColumns += $"{id};{tripName};{busId};{driverId};{conductorId};\n";
}
File.WriteAllText("trips.csv", tripColumns);