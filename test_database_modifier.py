"""
    KootNet Sensors is a collection of programs and scripts to deploy,
    interact with, and collect readings from various Sensors.  
    Copyright (C) 2018  Chad Ermacora  chad.ermacora@gmail.com  

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sqlite3
from guizero import App, Window, CheckBox, PushButton, Text, TextBox, MenuBar
from tkinter import filedialog

save_to_database = ""


def get_sql_data(var_column, var_table, var_start, var_end, conn_db):
    print("\nvar_column " + str(var_column))
    print("var_table " + str(var_table))
    print("var_start " + str(var_start))
    print("var_end " + str(var_end))
    print("conn_db " + str(conn_db))

    var_sql_query = "SELECT " + str(var_column) + " FROM " + str(var_table) + " WHERE Time BETWEEN date('" + str(var_start) + "') AND date('" + str(var_end) + "')"

    try:
        conn = sqlite3.connect(str(conn_db))
        c = conn.cursor()
    except:
        print("Failed DB Connection")
    
    try:
        c.execute(var_sql_query)
        var_sql_data = c.fetchall()
        count = 0
        for i in var_sql_data:
            var_sql_data[count] = str(var_sql_data[count])[2:-3]
            count = count +1

    except:
        print("Failed SQL Query Failed")
        
    if var_column == "hatTemp":
        count = 0
        for i in var_sql_data:
            var_sql_data[count] = str(int(var_sql_data[count]) - 4)
            count = count + 1
        
    c.close()
    conn.close()
    
    return var_sql_data


def extract_database(sql_start, sql_end):
    tmp_textbox_log1 = "\nStarting DataBase Extraction\n"
    j = filedialog.askopenfilename()

    try:
        var_Time = get_sql_data('Time','Sensor_Data',sql_start,sql_end,j)
        var_hostName = get_sql_data('hostName','Sensor_Data',sql_start,sql_end,j)
        var_uptime = get_sql_data('uptime','Sensor_Data',sql_start,sql_end,j)
        var_ip = get_sql_data('ip','Sensor_Data',sql_start,sql_end,j)
        var_cpuTemp = get_sql_data('cpuTemp','Sensor_Data',sql_start,sql_end,j)
        var_hatTemp = get_sql_data('hatTemp','Sensor_Data',sql_start,sql_end,j)
        var_pressure = get_sql_data('pressure','Sensor_Data',sql_start,sql_end,j)
        var_humidity = get_sql_data('humidity','Sensor_Data',sql_start,sql_end,j)
        var_lumens = get_sql_data('lumens','Sensor_Data',sql_start,sql_end,j)
        var_red = get_sql_data('red','Sensor_Data',sql_start,sql_end,j)
        var_green = get_sql_data('green','Sensor_Data',sql_start,sql_end,j)
        var_blue = get_sql_data('blue','Sensor_Data',sql_start,sql_end,j)
        tmp_textbox_log1 = tmp_textbox_log1 + "\nSQL Data Extracted OK"
        return var_Time, var_hostName,var_uptime,var_ip,
        var_cpuTemp,var_hatTemp,var_pressure,var_humidity,
        var_lumens,var_red,var_green,var_blue
        
    except:
        tmp_textbox_log1 = tmp_textbox_log1 + "\nSQL Data Extraction Failed"


def save_to():
    save_to_database = filedialog.askopenfilename()


def combine_database():
    print("hey")

app2 = App(title="Sensor Graph DataBase Modifier", width=375, height=300, layout="grid")

button_db1 = PushButton(app2, text="New Database", \
                           command = combine_database, grid=[1,1], align="left")
button_db2 = PushButton(app2, text="Add Database", \
                           command = combine_database, grid=[2,1], align="left")
button_db2.disable()
button_db3 = PushButton(app2, text="Save Database", \
                           command = combine_database, grid=[3,1], align="left")
button_db3.disable()


app2.display()
