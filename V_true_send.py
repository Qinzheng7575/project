import struct
import platform

def ToBytes(a):
    return struct.pack('>i',a)

CFG=[]
# CFG.append(ToBytes(0))
# CFG.append(ToBytes(2))
# CFG.append(ToBytes(1))
# CFG.append(ToBytes(0))#CFG(stack, antennaMode, 0)
# CFG.append(ToBytes(0))
# CFG.append(ToBytes(1))#CFG(stack, main_node, 1)
# CFG.append(ToBytes(1))#CFG(stack, gps_enable, 0)
# CFG.append(ToBytes(0))# CFG(stack, continuous_transceive, 0)
# CFG.append(ToBytes(1))# CFG(stack, coastas_loop_enable, 1)
# CFG.append(ToBytes(0))
# CFG.append(ToBytes(1))#CFG(test, slot_interval, 1)
#V段接收者：
# CFG.append(ToBytes(0))
# CFG.append(ToBytes(2))
# CFG.append(ToBytes(2))
# CFG.append(ToBytes(0))#CFG(stack, antennaMode, 0)
# CFG.append(ToBytes(0))
# CFG.append(ToBytes(1))#CFG(stack, main_node, 1)
# CFG.append(ToBytes(1))#CFG(stack, gps_enable, 0)
# CFG.append(ToBytes(0))# CFG(stack, continuous_transceive, 0)
# CFG.append(ToBytes(1))# CFG(stack, coastas_loop_enable, 1)
# CFG.append(ToBytes(0))
# CFG.append(ToBytes(1))#CFG(test, slot_interval, 1)
#S段发送者
# CFG.append(ToBytes(0))
# CFG.append(ToBytes(7))
# CFG.append(ToBytes(1))
# CFG.append(ToBytes(0))#CFG(stack, antennaMode, 0)
# CFG.append(ToBytes(0))
# CFG.append(ToBytes(1))#CFG(stack, main_node, 1)
# CFG.append(ToBytes(1))#CFG(stack, gps_enable, 0)
# CFG.append(ToBytes(0))# CFG(stack, continuous_transceive, 0)
# CFG.append(ToBytes(1))# CFG(stack, coastas_loop_enable, 1)
# CFG.append(ToBytes(0))
# CFG.append(ToBytes(1))#CFG(test, slot_interval, 1)

#S段接收者
CFG.append(ToBytes(0))
CFG.append(ToBytes(7))
CFG.append(ToBytes(2))
CFG.append(ToBytes(0))#CFG(stack, antennaMode, 0)
CFG.append(ToBytes(0))
CFG.append(ToBytes(1))#CFG(stack, main_node, 1)
CFG.append(ToBytes(1))#CFG(stack, gps_enable, 0)
CFG.append(ToBytes(0))# CFG(stack, continuous_transceive, 0)
CFG.append(ToBytes(1))# CFG(stack, coastas_loop_enable, 1)
CFG.append(ToBytes(0))
CFG.append(ToBytes(1))#CFG(test, slot_interval, 1)

for i in range(36):
    CFG.append(ToBytes(0))

# UDP=b'\xeb\x90\x17\x06'
UDP=b'\xeb\x90\x17\x01'

for i in CFG:
    UDP+=i

# print(UDP,len(UDP))
print('Windows' in platform.platform())


