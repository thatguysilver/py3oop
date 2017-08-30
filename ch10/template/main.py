class QueryTemplate:
    '''
    Our base class. All of its child classes will diverge from this point in 
    functionality, but in this template example, the commonality between the
    classes -- that is, that they will both connect, construct a query,
    format the results and then output those results -- is contained in this
    class. This is the essence of the template design pattern.
    '''
    def connect(self):
        self.conn = sqlite3.conect('sales.db')
    
    def construct_query(self):
        raise NotImplementedError()
    
    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(', '.join(row))
        self.formatted_results = '\n'.join(output)

    def output_results(self):
        raise NotImplementedError()

    def process_format(self):
        'Callling this ensures that procedure for a lookup follows the proper order.'
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()

import datetime 

class NewVehiclesQuery(QueryTemplate):
    def construct_query(self):
        self.query = 'select * from Sales where new = "true"'

    def output_results(self):
        print(self.formatted_results)

class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = ('select salesperson, sum(amt ' + 
                ' from Sales group by salesperson')

    def output_results(self):
        filename = 'gross_sales_{0}'.format(
                datetime.date.today().strftime('%Y%m%d')
                )
        with open(filename, 'w') as outfile:
            outfile.write(self.formatted_results)
