#freecon_webscraper.py

## EXTERNAL DEPENDENCIES
import re as eX_REG
#import asyncio	as eX_ASY					# For Async. File IO for Python

import pandas as eX_PAD

import requests as eX_REQ
from requests import get as eX_GET
from bs4 import BeautifulSoup as eX_BS4		# For manipulating HTML & XML files

# import selenium as eX_SEM					# For manipulating a web browser
from selenum import webdriver as eX_WEBDR


## GLOBALS
DRtypes = { "firefox" : eX_WEBDR.Firefox ,
			"chrome": eX_WEBDR.Chrome 				}
current_DRtype = None
modes = { 	"youtube": run_youtube_procedures, 
			"twitter": run_twitter_procedures, 
			"facebook": run_facebook_procedures,
			"reddit": run_reddit_procedures			}
keywords = []
current_URL = 0
task_script = []

URLs = [""]
client = None


### Youtube Specific
parsed_data_repository["youtube"] = {}
current_relevent_video_URLs = []
total_videos_processed = 0
total_related_user_profiles_processed = 0


## CLASS DECLARATIONS
class Scraper () :
	driver = None 
	def __init__ (self,driver_type) :
		driver = driver_types[driver_type]()
		self.run()
	def run() :
		while (True) :
			modes[current_mode]()
		self.terminate()
	def terminate() :
		if (driver != None) : 
			driver.close()
	def change_driver_type (self,DRtype,DRoptions,DRpath) :
		if ( driver != None ) : 
			driver.close()

		if ( DRoptions != None && DRpath != None ) :
			driver = DRtypes[DRtype](ptions=DRoptions,path=DRpath)
		else if ( DRoptions != None && DRpath == None )
			driver = DRtypes[DRtype](options=DRoptions)	
		else if ( DRpath != None )
			driver = DRtypes[DRtype](path=DRpath)
		else 
			driver = DRtypes[DRtype]()

	def run_youtube_operations(script_path) :
		script = open(script_path)
		operations = { 	"get_video_URLs" : search_for_youtube_videos
						"scrape_videos" : scrape_youtube_videos
						"scrape_user_profile" : scrape_youtube_user_profiles }
		while (True) :
			script[0](script[1])
			script[0].pop()
			script[0].pop()


		# import keywords
		# do a youtube search 
			# from the search, extract the URL from each link to each video
			# extract these links to a simple array
	
		# dispatch workers for video URLs
		# begin accessing individual videos
			# wait for the randomized access-wait interval to conlude
			# try to access video URL
				# if failed, remove & append to back, then add wait time
				# if succeeded, extract the comments & a url link to each account (key)
			# repeat until video URLs are exhausted
	
		# dispatch workers for user_profile URLs
		# begin trying to access individual user accounts
			# wait for the randomized access-wait interval to conlude
			# try to access the user URL
				# if failed, remove & append to back, then add wait time
				# if succeeded, extract the relevent statistics regarding the video
			# repeat until the user URLs are a exhausted

		# parse and dump data into workable plain text (CSV,TSV,LSV,SSV)

	def search_for_youtube_videos( params ) :
		if (driver != None) : 
			driver.close()
			configurations = None
		if (current_DRtype == "Chrome")
			configurations = driver.ChromeOptions()
			configurations.add_argument( "start-maximized" )
			configurations.add_experimental_option( "excludeSwitches" , ["enable-automation"] )
			configurations.add_experimental_option( 'useAutomationExtension' , False  )
			change_driver_type("Chrome")

	def get_video_statistics( params ) :
		driver.get("https://socialblade.com")

	def scrape_youtube_comment( params ) :
		driver.get('http://youtube.com/watch?v='+params[0])
		driver.execute_script('return scrollBy(0,400);')
		subscribe = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,
			"//yt-formatted-string[text()='Subscribe']")))
		driver.execute_script('arguements[0].scrollIntoView(true)',subscribe)
		comments = []
		subscribe = WebDriverWait(driver)
		my_length = len( WebDriverWait(driver,20).until(EC.visibility_of_all_element((By.XPATH,
			"//yt-formatted-string[@class='style-scope ytd-comment-renderer' and @id='content-text'][@slot='content']"))))
		while ( True ) :	
			try : 
				driver.execute_script('window.scrollBy(0,800)')
				time.sleep(5)
			except TimeoutException :
				break

		# Maybe add assert statements
		


		keywords = keywords[topic]
		driver.get(f'{baseline_URL}/search?q={keyword}')

		driver.quit()

	def scrape_youtube_video( video_URL ) :
		content.requests.get(current_URL+video_URL)
		parser = BeautifulSoup(content.text,"html.parser")
		video = {}
		video["video_title"] = ?
		video["channel_title"] = content.h3.a.text
		video["view_count"] = ?
		video["likes"] = ?
		comment_count = ?
		for comment in range(0,comment_count) :
			current = {}
			current["username"] = parser.find(?)
			current["user_metadata_URL"] = parser.find(?)
			current["content"] = parser.find(?)
			current["likes"] = parser.find(?)
			#...
			video["comment "+comment] = []
		parsed_data_repository["youtube"]["video "+total_videos_processed] = video

	def scrape_user_profiles( video_URL ) :


class Worker () :
	def __init__(self) :

	def initialize() :
	def conduct_task() :
	def terminate() :	




def run(execution_scheme) :
	while(True) :
		# maybe create worker classes to run asynchronous scrapers

		if ( current_mode ) 

		# if mode = "youtube"
			





def set_URL(URL):
	current_URL = URL
	client.urlopen(current_URL)

def close_client():
	client.close()

def set_keywords():
def remove_key_text():

def fetch_html():
	webpage = client.read()
def parse_html():
	in


def dump_parsed_data()


def fetch_user_metadata():


def search_twitter_hashtags():
def process_twitter_groups():

def search_facebook_groups():
def search_facebook_group_posts():