#freecon_suite.py

## EXTERNAL DEPENDENCIES
import os as eX_SYS
import datetime as eX_CRO
import pandas as eX_PND
import numpy as eX_NPY
#import asyncio	as eX_ASY					# For Async. File IO for Python

## INTERNAL DEPENDENCIES
import freeconWS_web_scraper as iN_WSC
import freeconWS_NL_parser as iN_NLP
import freeconWS_database_interface as iN_DBN

## GLOBALS
# Task Queue
tskq = []						# task_queue
cur = 0							# current_index

# Buffers
buffers = { "default","" }		# data_buffer
bf_sel = 0						# selected_buffer
bf_count = 0					# buffer_count

# Flags
prompt_user = true 
backup_buffers = false
CLI_feedback = true

# Task Switcher
tasks = {	0 , exit_suite 
			1 , toggle_feedback
			2 , toggle_buffer_backups

			3 , add_buffer
			4 , delete_buffer
			5 , purge_buffer
			6 , peek_buffer_content
			7 , gage_buffer_size

			8 , scrape_for_data

			9 , parse_data

			10 , convert_buffer_data_to_csv

			11 , push_buffer_data_to_database
			12 , pull_from_database_to_buffer
			13 , dump_from_database_to_csv
			14 , delete_table_from_database	
			15 , purge_entire_database			}

task_parameters = []
task_count = len(task)


### FUNCTION DEFINTIONS
def interpert_taskflow():
	# Task Source
	# If on CLI "file:"

	# Else
		# switch to basic macro_task_bundles
	# fall-through Else
		# use as a custom bundle
			# include manual case
	# else
		# throw error, prompt for manual

def exit_suite():
	prompt_user = false
	#
def toggle_buffer_backups():
	if backup_buffers is false :
		backup_buffers = true
	else :
		backup_buffers = false
def toggle_feedbeck():
	if CLI_feedback is false :
		CLI_feedback = true
	else :
		CLI_feedback = false

def add_buffer():
	if buffers.get(task_parameters[1]) is None : 
		buffers.update({task_parameters[1]:""})
		feedback ("$$:...new buffer created : \""+task_parameters[1]+"\"\n")
	else :
		feedback ("$$:...ERROR: buffer already exists.\n")
def remove_buffer():
	if buffers.get(task_parameters[1]) is None : 
		feedback ("$$:...ERROR: buffer not found.\n")
	else :
		buffers.pop({task_parameters[1]:""})
		feedback ("$$:...buffer removed : \""+task_parameters[1]+"\"\n")
def purge_buffer():
	if buffers.get(task_parameters[1]) is None : 
		feedback ("$$:...ERROR: buffer not found.\n")
	else :
		buffers.update({task_parameters[1]:""})
		feedback ("$$:...buffer content purged : \""+task_parameters[1]+"\"\n")
def peek_buffer_content():
	if buffers.get(task_parameters[1]) is None : 
		feedback ("$$:...ERROR: buffer not found.")
	else :
		feedback ("$$:...Contents of buffer \""+task_parameters[1]+"\" :\n")
		print("+====================================+\n")
		print(buffers[task_parameters[1]])
		print("+====================================+\n")
def gage_buffer_size():
	if buffers.get(task_parameters[1]) is None : 
		feedback ("$$:...ERROR: buffer not found.")
	else :
		feedback ("$$:...Characters in buffer \""+task_parameters[1]+"\": ")
		print(len(buffers[task_parameters[1]]))

def scrape_for_data():
	#prompt with options for when to pull and when to parse
	#provide idea of data amounts / usage while processing
	#prompt for which buffer to draw to, or to use a new one

def parse_data():
	#prompt for which buffer to draw from
	#provide idea of data amounts / usage currently in selected buffer, then prompt for confimation
	#allow partial amount of buffer to be emptied
	#...also provide an estimate of time need to complete based on system profile

def convert_buffer_data_to_csv():

def push_data_buffer_to_database():
	#prompt for which buffer to draw from
	#provide idea of data amounts / usage currently in selected buffer
	#...also provide an estimate of time need to complete based on system profile
def convert_data_to_csv():
	#prompt for which buffer to draw from
	#prompt with summary of data_size and time needed for processing
def pull_data_from_database():
	#prompt for which buffer to draw to
	#prompt with summary of data_size and time needed for processing
	#overwrite buffer?
	#directly to csv?
def dump_the_database_to_csv():
def delete_table_from_database():
def purge_entire_database():

def backup_buffers():
	filename = "backups"+eX_CRO.timestamp()
	eX_SYS.mkdir(filename)
	eX_SYS.chdir( eX_SYS.getcwd()+"\""+filename)
	for buf in buffers :
		buffers.

	eX_SYS.chdir()
def import_backup_buffers():	
def feedback(str) :
	if CLI_feedback is True :
		print(str)
def main():
	feedback("$:...freeconWS has initalized...")
	while True:
		while len(tskq) is not 0:
			feedback("$:......processing task... "+cur)
			feedback("$:.........selecting buffer "+tsk1[0][1]" : "+buffers[tsk1[0][1]]+"...")
			bf_sel = tsk1[0][1]
			feedback("$:.........applying parameters...")
			parameters = tskq[0][2]
			feedback("$:.........conducting \""+task+"\"...")
			task[tskq[0][0]]
			tskq.pop(0)
		feedback("$:...no outstanding tasks remaining...")

		while prompt_user is True :
			feedback("$:.........consulting user...")
			while True :
				feedback("$$:...(What Next?) :\n" + task_marquee)
				raw = input("\n >> ")
				raw.split(" ")
				if (raw_input[0] in range(task_count)):
					task = raw[0]
					raw.pop(0)
					tskq.append(task,raw)
					break
				else 
					feedback ("$$:...ERROR: Task not found/defined.")
			if( tskq[0] is not 0 ) :
				continue

		if buffer_backup is true :
			backup_buffers()

		break
	feedback("$:...freeconWS has concluded operations.")

### EXECUTION / ENTRY POINT
interpert_taskflow()
main()

