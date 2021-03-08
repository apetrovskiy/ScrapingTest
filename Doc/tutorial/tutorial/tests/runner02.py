import subprocess
process = subprocess.Popen(['cd ../..', 'scrapy crawl quotes3'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
stdout, stderr