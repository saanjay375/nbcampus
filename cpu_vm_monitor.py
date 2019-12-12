import psutil

print ('Executing CPU and Virtual Memory utilization script')

print ('Printing current CPU Utilization : %s' % (psutil.cpu_percent()) )

print ('Printing current Virtual Memory Utilization : %s' %(dict(psutil.virtual_memory()._asdict()) ) )
