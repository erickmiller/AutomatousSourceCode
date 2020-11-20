import rpyc

rpyc.core.protocol.DEFAULT_CONFIG['allow_pickle'] = True

def square(x):
    return x*x

c = rpyc.connect("localhost", port = 18861, config = rpyc.core.protocol.DEFAULT_CONFIG)

for i in range(0, 1):
    result = c.root.exposed_RemotePool(square, [0,1,2,3])
    print(result)