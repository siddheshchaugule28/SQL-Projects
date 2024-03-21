import mysql.connector

# Create a class DB
class DB:
    # Create constructor
    def __init__(self):
        # connect to the database server 
        try:
            self.conn=mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='flight'
            )

            self.mycursor=self.conn.cursor()
            print("Connection Established")
        except:
            print("Connection Error")

# """ create a method inside a class that will execute a query to fetch
#  all distinct destinations and Source """

    def fetch_city_names(self):
        city=[]
        self.mycursor.execute("""
        select distinct(destination) from flights
        union 
        select distinct(Source) from flights
        """)

        data= self.mycursor.fetchall()
        
        for item in data:
            city.append(item[0])

        return city
# Create a method to show all the flights available 
# for the selected Source and Destination

    def fetch_all_flights(self,Source,Destination):
        self.mycursor.execute("""
                        select Airline,Route,Dep_Time from flights
                        where Source="{}" and Destination="{}"
                        """.format(Source,Destination)
        )

        data= self.mycursor.fetchall()

        return data

# """ create a method that will return two lists airline and frequency
#  to plot a graph(pie chart)"""

    def fetch_airlin_frequency(self):

        airline=[]
        frequency=[]

        self.mycursor.execute("""
                        select Airline,count(*) from flights
                        group by Airline
                        """
        )
        data= self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency

# """ create a method that will return two lists city and frequency
# to plot a bar graph """
    def busy_airport(self):

        city=[]
        frequency=[]

        self.mycursor.execute("""
                        select Source,count(*) from 
                                            (select Source from flights
                                            union all 
                                            select Destination from flights) t
                        group by t.Source
                        order by count(*) DESC
                        """
        )
        data= self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city,frequency