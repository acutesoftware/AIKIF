# cls_sql_code_generator.py written by Duncan Murray June 2014

"""
usage from other programs:
    from sql_code_generator import SQLCodeGenerator
    tst = SQLCodeGenerator('C_FACT_TABLE')
    print(tst)

"""


class SQLCodeGenerator(object):
    """ generates SQL based on a table  """
    def __init__(self, fact_table):
        self.fact_table = fact_table
        self.sql_text = ''      # for the main procedure
        self.ddl_text = ''      # for the create scripts
        self.col_list = []

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
   
    def save_ddl(self, fname):
        with open(fname, "w") as f:
            f.write(self.ddl_text)
    
    def set_column_list(self, col_list):
        """ 
        opens table or CSV file and collects column names, data samples
        set_column_list(['yr', 'institution', 'gender', 'count_completions'])
        """
        self.col_list = col_list
     
    def add_to_column_list(self, col_list):
        """ 
        opens table or CSV file and collects column names, data samples
        set_column_list(['yr', 'institution', 'gender', 'count_completions'])
        """
        self.col_list.extend(col_list)
     
    def get_column_list_from_select(self, txt, col_delim=','):
        """ 
        takes the list of columns as a string (via SELECT statement in DB)
        and produces a lst of columns
        """
        return [c.strip().strip(',') for c in txt.split(col_delim)]
    
    def create_script_fact(self):
        """
        appends the CREATE TABLE, index etc to self.ddl_text
        """
        self.ddl_text += '---------------------------------------------\n'
        self.ddl_text += '-- CREATE Fact Table - ' + self.fact_table + '\n'
        self.ddl_text += '---------------------------------------------\n'
        self.ddl_text += 'DROP TABLE ' + self.fact_table + ' CASCADE CONSTRAINTS;\n'
        self.ddl_text += 'CREATE TABLE ' + self.fact_table + ' (\n'
        self.ddl_text += ' '.join([col + ' VARCHAR2(200), \n' for col in self.col_list])
        self.ddl_text += ' REC_EXTRACT_DATE  DATE \n' # + src_table + '; \n'
        self.ddl_text += ');\n'
    
    def create_script_staging_table(self, output_table, col_list):
        """
        appends the CREATE TABLE, index etc to another table
        """
        self.ddl_text += '---------------------------------------------\n'
        self.ddl_text += '-- CREATE Staging Table - ' + output_table + '\n'
        self.ddl_text += '---------------------------------------------\n'
        self.ddl_text += 'DROP TABLE ' + output_table + ' CASCADE CONSTRAINTS;\n'
        self.ddl_text += 'CREATE TABLE ' + output_table + ' (\n'
        self.ddl_text += ' '.join([col + ' VARCHAR2(200), \n' for col in col_list])
        self.ddl_text += ' REC_EXTRACT_DATE  DATE \n' # + src_table + '; \n'
        self.ddl_text += ');\n'
    
    def create_index(self, tbl, col_list ):
        self.ddl_text += '\nCREATE INDEX ndx_' + tbl + ' ON ' + tbl + ' ('
        self.ddl_text += ','.join([c for c in col_list]) + ' );\n' 
    
    
    
    def trunc_fact_table(self):
        """ wipe all records from fact table """
       	self.sql_text += 'DELETE FROM ' + self.fact_table + ';\n'
        self.sql_text += 'COMMIT;\n'
       
    def reverse_pivot_to_fact(self, staging_table, piv_column, piv_list, from_column, meas_names, meas_values, new_line):
        """
        For each column in the piv_list, append ALL from_column's using the group_list
        e.g.
            Input Table
            YEAR    Person    Q1    Q2    
            2010    Fred    Spain   14
            2010    Jane    Spain   13.995
            
            Output Table
            Year    Person   Question    Result
            2010    Fred        Q1           Spain
            2010    Fred        Q2           14
            2010    Jane        Q1           Spain
            2010    Jane        Q2           13.995
            
            You would use:
                from_column  = [YEAR, Person]
                pivot_column = 'Question'
                piv_list     = [Q1, Q2]
                meas_names   = [Result]
                meas_values  = [Result]   # this can be SQL such as count(*) or count(distinct COL_NAME)
                
        To get the result:
            INSERT INTO C_UES2014_FT (
            YEAR, Person, Question, Result, REC_EXTRACT_DATE) (
            SELECT 
            YEAR, Person, 'Q1', Q1, SYSDATE 
                FROM S_UES2014_RAW);
            INSERT INTO C_UES2014_FT (
            YEAR, Person, Question, Result, REC_EXTRACT_DATE) (
            SELECT 
            YEAR, Person, 'Q2', Q2, SYSDATE 
                FROM S_UES2014_RAW);
            COMMIT;        
        """
        self.sql_text += '\n-----------------------------\n--Reverse Pivot\n--------------------------\n\n'
        num_chars_on_line = 0
        for piv_num in range(len(piv_list)):
            # INSERT columns
            self.sql_text += 'INSERT INTO ' + self.fact_table + ' (' + new_line
            if piv_column not in from_column:
                self.sql_text += piv_column + ', '
                #pass
            for g in meas_names:
                self.sql_text += g + ', '
            
            for c in from_column:
                if c not in meas_names:
                    if c == piv_column: # dont insert the same column twice
                        print("Error - do NOT specify pivot column in the fact list")
                        exit(1)
                    else:
                        self.sql_text += c + ', '
                        num_chars_on_line += len(c) + 2
                        if num_chars_on_line > 100:
                            self.sql_text +=  new_line
                            num_chars_on_line = 0
            self.sql_text += 'REC_EXTRACT_DATE) (\n' 
                        
            
            # SELECT columns
            self.sql_text += 'SELECT '  + new_line
            num_chars_on_line = 0
            self.sql_text += "'" + piv_list[piv_num] + "', "
            for meas_num, meas_name in enumerate(meas_names):
                if meas_values[meas_num] == '':
                    self.sql_text += piv_list[piv_num] + ', '
                else:
                    self.sql_text += meas_values[meas_num] + ', '
                
            for c in from_column:
                if c not in meas_names: # dont insert the same column twice
                    self.sql_text += c + ', '
                    num_chars_on_line += len(c) + 2
                    if num_chars_on_line > 100:
                        self.sql_text +=  new_line
                        num_chars_on_line = 0
                
            self.sql_text += 'SYSDATE \nFROM ' + staging_table
            self.sql_text += ');\n'

        
       
    def populate_from_staging(self, staging_table, from_column_list, output_table):
        """ 
        generate SQL to insert staging table records into
        the core table based on column_list (If no column list
        then insert sequentially)
        """
        self.sql_text += 'INSERT INTO ' + output_table + ' (\n'
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
 
 
    def collect_stats(self, tbl):
        self.sql_text += "collect_stats('" + tbl + "'); \n"
 
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
        UPDATE c_aup_compl op SET op.gender_key = NVL ( (SELECT MAX (ip.gender_key)
          FROM edw.u_cfm_gender_c ip WHERE ip.gender_code = SUBSTR (op.gender, 1, 1)), -1);
        """
        
        self.sql_text += "UPDATE " + self.fact_table + " op SET op." + fact_key + " = NVL(\n"
        self.sql_text += "  (SELECT MAX (ip." + dimension_key + ")\n"
        self.sql_text += "    FROM " + dimension_name + " ip WHERE "
        self.sql_text += fact_join_col + " = \n       ip." + dimension_join_col + "), -1); \n\n"
        
    def extract_dimension(self, dim_name, dim_cols, dim_key, dim_stag_table, src_table, src_cols, grain_cols, where_clause):
        """
        selects the src_cols from src_table and groups by dim_grain
        then inserts into newly created table dim_name the columns as 'dim_cols
        """
        
        self.ddl_text += '---------------------------------------------\n'
        self.ddl_text += '-- CREATE Dimension - ' + dim_name + '\n'
        self.ddl_text += '---------------------------------------------\n'
        self.ddl_text += 'DROP TABLE ' + dim_stag_table + ' CASCADE CONSTRAINTS;\n'
        self.ddl_text += 'CREATE TABLE ' + dim_stag_table + ' (\n'
        self.ddl_text += ' '.join([col + ' VARCHAR2(200), \n' for col in dim_cols])
        self.ddl_text += ' REC_EXTRACT_DATE  DATE \n' # + src_table + '; \n'
        self.ddl_text += ');\n'
        
        self.ddl_text += 'DROP TABLE ' + dim_name + ' CASCADE CONSTRAINTS;\n'
        self.ddl_text += 'CREATE TABLE ' + dim_name + ' (\n'
        self.ddl_text += ' ' + dim_key + ' NUMBER, \n'
        self.ddl_text += ' '.join([col + ' VARCHAR2(200), \n' for col in dim_cols])
        self.ddl_text += ' REC_SOURCE_SYSTEM  VARCHAR2(100), \n' # + src_table + '; \n'
        self.ddl_text += ' REC_EXTRACT_DATE  DATE \n' # + src_table + '; \n'
        self.ddl_text += ');\n'
        self.ddl_text += 'CREATE OR REPLACE VIEW U' + dim_name[1:] + ' AS SELECT * FROM ' + dim_name + ';\n'
        self.ddl_text += 'GRANT SELECT ON U' + dim_name[1:] + ' TO EDW_STUDENT;\n'
        self.ddl_text += '\n'
        self.ddl_text += 'DROP SEQUENCE SEQ_' + dim_name + ';\n'
        self.ddl_text += 'CREATE SEQUENCE SEQ_' + dim_name + ';\n\n'
        
        
        self.sql_text += '---------------------------------------------\n'
        self.sql_text += '-- Populate Dimension - ' + dim_name + '\n'
        self.sql_text += '---------------------------------------------\n'
        self.sql_text += "DELETE FROM " + dim_stag_table + ";\n"
        self.sql_text += "COMMIT;\n"
        self.sql_text += "INSERT INTO " + dim_stag_table + " (\n"
        self.sql_text += ", ".join([col for col in dim_cols])
        self.sql_text += ")\n (SELECT \n"
        self.sql_text += ", ".join([col for col in src_cols])
        self.sql_text += "\nFROM " + src_table + "\n"
        if where_clause != '':
            self.sql_text += "WHERE " + where_clause + "\n"
        if len(grain_cols) > 0:
            self.sql_text += "GROUP BY " + ", ".join([col for col in grain_cols]) + "\n"
        self.sql_text += "); \n"
        self.sql_text += "COMMIT;\n"
        
        
        self.sql_text += "DELETE FROM " + dim_name + ";\n"
        self.sql_text += "COMMIT;\n"
        self.sql_text += "INSERT INTO " + dim_name + " (\n"
        self.sql_text += ", ".join([col for col in dim_cols])
        self.sql_text += ", REC_SOURCE_SYSTEM, REC_EXTRACT_DATE "
        
        self.sql_text += ") \n(SELECT \n"
        self.sql_text += ", ".join([col for col in src_cols])
        self.sql_text += ", '" + src_table + "', sysdate "
        self.sql_text += "\nFROM " + dim_stag_table + "\n"
        self.sql_text += "); \n"
        self.sql_text += "COMMIT;\n"
        
        self.sql_text += "UPDATE " + dim_name + " SET " + dim_key + " = SEQ_" + dim_name + ".nextval;\n"
        self.sql_text += "COMMIT;\n\n"
        
        
        print(self.ddl_text)
        print(self.sql_text)
        
    def aggregate(self, opTable, group_by_cols, meas):
        """ 
        Create an aggregate table grouped by col showing meas
        The meas is something like "sum(in)" or "count(*)"
        RETURNS:
            DROP TABLE C_AGG_PRODUCT;
            CREATE TABLE C_AGG_PRODUCT AS (
                SELECT PRODUCT, sum(AMOUNT) AS result 
                FROM C_SALES GROUP BY PRODUCT
            );

        """
        self.sql_text += "DROP TABLE " + opTable + ";\n"
        self.sql_text += "CREATE TABLE " + opTable + " AS (\n"
        self.sql_text += "    SELECT " + group_by_cols + ", " + meas + " AS result \n"
        self.sql_text += "    FROM " + self.fact_table + " GROUP BY " + group_by_cols + "\n"
        self.sql_text += ");\n"        
        