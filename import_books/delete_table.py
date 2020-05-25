from models import *
from sqlalchemy import *

engine = create_engine('postgres://gqymvscekvfgty:44c3422f56f15fdfe08f2d8d4e1652c98be6b87fca411ca898f96bbe5f94d0ab@ec2-176-34-97-213.eu-west-1.compute.amazonaws.com:5432/d2afn869tf1fcb')
'''table name'''
#input_N=input('Enter Teble Name')  
#input_N.__table__.drop(engine)
Review.__table__.drop(engine)