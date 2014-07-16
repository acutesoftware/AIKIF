# form_example_simple.py    written by Duncan Murray 16/7/2014

import os
import sys
import math
import time
import tkinter
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep ) 

def main():
    frame = tkinter.Tk()
    frame.geometry("600x200")
# see http://stackoverflow.com/questions/21894947/tkinter-press-enter-in-entry-box-append-to-text-box-how
    lbl_title = tkinter.Label(frame, text="SQL Generator").grid(row=1, column=1, sticky="E")
    
    lbl_name = tkinter.Label(frame, text="Enter output File").grid(row=2, column=1, sticky="E")
    lbl_proj = tkinter.Label(frame, text="Proj ID").grid(row=3, column=1, sticky="E")
    lbl_tbl = tkinter.Label(frame, text="Table name").grid(row=4, column=1, sticky="E")
    lbl_tbl = tkinter.Label(frame, text="List of Columns").grid(row=5, column=1, sticky="E")
    txt_file = tkinter.Entry(frame,width=30)
    txt_file.grid(row=2, column=2, sticky="W")
    txt_proj = tkinter.Entry(frame,width=30)
    txt_proj.grid(row=3, column=2, sticky="W")
    txt_tbl = tkinter.Entry(frame,width=30)
    txt_tbl.grid(row=4, column=2 ,sticky="W")

    txt_cols = tkinter.Entry(frame,width=80)
    txt_cols.grid(row=5, column=2, sticky="W")
    
    txt_sql = tkinter.Text(frame,  width=60, height=5)
    txt_sql.grid(row=8, column=2)
    S = tkinter.Scrollbar(frame)
    txt_file.insert(0, "my_generated.sql")
    txt_proj.insert(0, "MY_PROJECT")
    txt_tbl.insert(0, "C_SALES_DATA")
    txt_cols.insert(0, "customer_key, product_key, date_key, store_key")
    btn = tkinter.Button(frame, text="Generate SQL", command=lambda: generate_sql(txt_sql, txt_proj.get(), txt_file.get(), txt_tbl.get(), txt_cols.get()))
    btn.grid(row=8, column=1,sticky="N")
    #frame.grid(sticky=tkinter.NSEW)
    frame.mainloop()
    
def generate_sql(text_box, fname, proj_id, tbl_name, cols):
    print("Generating SQL for proj", proj_id, " using table ", tbl_name, ", to fname ", fname)
    sql = []
    col_list = cols.split(',')
    for col in col_list:
        sql.append("SELECT count(distinct " + col.strip() + ") FROM " + tbl_name)
    text_box.insert(tkinter.END,"\n".join([l for l in sql]))
    with open(root_folder + os.sep + fname, "w") as f:
        f.write("\n".join([l for l in sql]))
    
    time.sleep(0.2)
    os.system("start " + fname )
main()    
    