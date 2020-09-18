#Import concurrent module for multiprocessing
import concurrent.futures

#import all the necessary functions to fetch the datas
from utils.toph import toph
from utils.dimikOJ import dimik
from utils.uri import uri

def fetchAll(tophLink, dimikLink, uriLink):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        t1 = executor.submit(toph, tophLink)
        t2 = executor.submit(dimik, dimikLink)
        t3 = executor.submit(uri, uriLink)

        tophSolved = t1.result()
        dimikSolved = t2.result()
        uriSolved = t3.result()
    return {
        "toph": tophSolved,
        "dimik": dimikSolved,
        "uri": uriSolved
    } 

