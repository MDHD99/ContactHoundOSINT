# Contact Hound- Contact OSINT
Contact Hound is an automated email gathering/notification delivery tool.

## Installation

```
$ git clone https://github.com/MDHD99/ContactHoundOSINT.git
$ cd ContactHoundOSINT/
$ python setup.py install
```
## Usage

For a single domain
```
python CHound.py -d example.com 
```

For using an input file and save results to an output file
```
python CHound.py -f domains.csv -t 2 -o results.csv
```
Example of type two input file:
![file2](https://github.com/MDHD99/ContactHoundOSINT/blob/master/images/file2.PNG)
Example output
![sampleout](https://github.com/MDHD99/ContactHoundOSINT/blob/master/images/termOUT.PNG)

### References
A part of the email gathering functions of this tool was based on infoga by [m4ll0k](https://github.com/m4ll0k)


