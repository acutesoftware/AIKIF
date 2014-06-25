# sql_code_generator.py
# usage from other programs
"""
from sql_code_generator import SQLCodeGenerator
tst = SQLCodeGenerator('C_FACT_TABLE')
print(tst)


"""


class SQLCodeGenerator(object):
    """ generates SQL based on a table  """
    def __init__(self, fact_table):
        self.fact_table = fact_table
        self.sql_text = ''

    def __str__(self):
        txt = self.fact_table + '\n'
        for col in self.col_list:
            txt += 'col : ' + col + '\n'
        return txt
    
    def get_sql(self):
        return self.sql_text
    
    def save(self, fname):
        with open(fname, "w") as f:
            f.write(self.sql_text)
    
    def set_column_list(self, col_list):
        """ 
        opens table or CSV file and collects column names, data samples
        set_column_list(['yr', 'institution', 'gender', 'count_completions'])
        """
        self.col_list = col_list
        
    def trunc_fact_table(self):
        """ wipe all records from fact table """
       	self.sql_text += 'DELETE FROM ' + self.fact_table + ';\n'
        self.sql_text += 'COMMIT;\n'
        
    def populate_from_staging(self, staging_table, from_column_list):
        """ 
        generate SQL to insert staging table records into
        the core table based on column_list (If no column list
        then insert sequentially)
        """
        self.sql_text += 'INSERT INTO ' + self.fact_table + ' (\n'
        for c in self.col_list:
            if c != '':
                self.sql_text += '    ' + c + ',\n'
        self.sql_text += '    REC_EXTRACT_DATE) (\n'
        self.sql_text += '    SELECT \n'
        for c in from_column_list:
            if c != '':
                self.sql_text += '        ' + c + ',\n'
        self.sql_text += '        SYSDATE \n    FROM ' + staging_table
        self.sql_text += '\n);\n'
 
    def comment(self, txt):
        self.sql_text += txt + '\n'
  
    def comment_block(self, txt):
        self.sql_text += '\n------------------------------------------------------------\n'
        self.sql_text += '--  ' + txt + '\n'
        self.sql_text += '------------------------------------------------------------\n\n'
 
    def update_old_to_new(self, col, old_val, new_val):
        """ simply updates all rows and sets COL to NEW_VAL where col = old_val
        e.g. update_old_to_new("NAME", "The University of Adelaide", "University of Adelaide")
        will generate
        UPDATE table op SET op.NAME = 'University of Adelaide' WHERE op.NAME = 'The University of Adelaide';
        """
        self.sql_text += "UPDATE " + self.fact_table + " SET " + col + " = '" + new_val + "' WHERE " + col + " = '" + old_val + "'; \n"
        
    def update_set_where(self, set_sql, where_sql):
        self.sql_text += "UPDATE " + self.fact_table + " SET " + set_sql + " WHERE " + where_sql + "; \n"
        
    def commit(self):
        self.sql_text += "COMMIT;\n"

 
    def key_to_dimension(self, fact_key, fact_join_col, dimension_name, dimension_join_col, dimension_key):
        """ 
        create SQL to join a fact table key based on "join_col" to a dimension 
        The fact table is aliased as "op" and the join dimension is aliased as "ip"
        meaning you can pass substrings or SQL to match values.
        e.g. the command:
        aup.key_to_dimension('GENDER_KEY', 'substr(op.GENDER, 1,1)', 'EDW.U_CFM_GENDER_C', 'gender_code', 'GENDER_KEY')

        will generate the code:
        UPDATE c_aup_compl op
           SET op.gender_key =
                  NVL ( (SELECT MAX (ip.gender_key)
                           FROM edw.u_cfm_gender_c ip
                          WHERE ip.gender_code = SUBSTR (op.gender, 1, 1)),
                       -1);
        """
        self.sql_text += "UPDATE " + self.fact_table + " op \n"
        self.sql_text += "    SET op." + fact_key + " = \n"
        self.sql_text += "        NVL ( (SELECT MAX (ip." + dimension_key + ")\n"
        self.sql_text += "                 FROM " + dimension_name + " ip \n"
        self.sql_text += "                WHERE ip." + dimension_join_col + " = " + fact_join_col + "), \n"
        self.sql_text += "             -1); \n"
        
