from aioconsole import ainput
from frameutils import Bluetooth
import asyncio
import time


header = bytearray(
    [
        0xFF,
        0xD8,
        0xFF,
        0xE0,
        0x00,
        0x10,
        0x4A,
        0x46,
        0x49,
        0x46,
        0x00,
        0x01,
        0x02,
        0x00,
        0x00,
        0x64,
        0x00,
        0x64,
        0x00,
        0x00,
        0xFF,
        0xDB,
        0x00,
        0x43,
        0x00,
        0x20,
        0x16,
        0x18,
        0x1C,
        0x18,
        0x14,
        0x20,
        0x1C,
        0x1A,
        0x1C,
        0x24,
        0x22,
        0x20,
        0x26,
        0x30,
        0x50,
        0x34,
        0x30,
        0x2C,
        0x2C,
        0x30,
        0x62,
        0x46,
        0x4A,
        0x3A,
        0x50,
        0x74,
        0x66,
        0x7A,
        0x78,
        0x72,
        0x66,
        0x70,
        0x6E,
        0x80,
        0x90,
        0xB8,
        0x9C,
        0x80,
        0x88,
        0xAE,
        0x8A,
        0x6E,
        0x70,
        0xA0,
        0xDA,
        0xA2,
        0xAE,
        0xBE,
        0xC4,
        0xCE,
        0xD0,
        0xCE,
        0x7C,
        0x9A,
        0xE2,
        0xF2,
        0xE0,
        0xC8,
        0xF0,
        0xB8,
        0xCA,
        0xCE,
        0xC6,
        0xFF,
        0xDB,
        0x00,
        0x43,
        0x01,
        0x22,
        0x24,
        0x24,
        0x30,
        0x2A,
        0x30,
        0x5E,
        0x34,
        0x34,
        0x5E,
        0xC6,
        0x84,
        0x70,
        0x84,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xC6,
        0xFF,
        0xC0,
        0x00,
        0x11,
        0x08,
            0x00,
            0xc8,
            0x00,
            0xc8,
        0x03,
        0x01,
        0x22,
        0x00,
        0x02,
        0x11,
        0x01,
        0x03,
        0x11,
        0x01,
        0xFF,
        0xC4,
        0x00,
        0x1F,
        0x00,
        0x00,
        0x01,
        0x05,
        0x01,
        0x01,
        0x01,
        0x01,
        0x01,
        0x01,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x01,
        0x02,
        0x03,
        0x04,
        0x05,
        0x06,
        0x07,
        0x08,
        0x09,
        0x0A,
        0x0B,
        0xFF,
        0xC4,
        0x00,
        0x1F,
        0x01,
        0x00,
        0x03,
        0x01,
        0x01,
        0x01,
        0x01,
        0x01,
        0x01,
        0x01,
        0x01,
        0x01,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x01,
        0x02,
        0x03,
        0x04,
        0x05,
        0x06,
        0x07,
        0x08,
        0x09,
        0x0A,
        0x0B,
        0xFF,
        0xC4,
        0x00,
        0xB5,
        0x10,
        0x00,
        0x02,
        0x01,
        0x03,
        0x03,
        0x02,
        0x04,
        0x03,
        0x05,
        0x05,
        0x04,
        0x04,
        0x00,
        0x00,
        0x01,
        0x7D,
        0x01,
        0x02,
        0x03,
        0x00,
        0x04,
        0x11,
        0x05,
        0x12,
        0x21,
        0x31,
        0x41,
        0x06,
        0x13,
        0x51,
        0x61,
        0x07,
        0x22,
        0x71,
        0x14,
        0x32,
        0x81,
        0x91,
        0xA1,
        0x08,
        0x23,
        0x42,
        0xB1,
        0xC1,
        0x15,
        0x52,
        0xD1,
        0xF0,
        0x24,
        0x33,
        0x62,
        0x72,
        0x82,
        0x09,
        0x0A,
        0x16,
        0x17,
        0x18,
        0x19,
        0x1A,
        0x25,
        0x26,
        0x27,
        0x28,
        0x29,
        0x2A,
        0x34,
        0x35,
        0x36,
        0x37,
        0x38,
        0x39,
        0x3A,
        0x43,
        0x44,
        0x45,
        0x46,
        0x47,
        0x48,
        0x49,
        0x4A,
        0x53,
        0x54,
        0x55,
        0x56,
        0x57,
        0x58,
        0x59,
        0x5A,
        0x63,
        0x64,
        0x65,
        0x66,
        0x67,
        0x68,
        0x69,
        0x6A,
        0x73,
        0x74,
        0x75,
        0x76,
        0x77,
        0x78,
        0x79,
        0x7A,
        0x83,
        0x84,
        0x85,
        0x86,
        0x87,
        0x88,
        0x89,
        0x8A,
        0x92,
        0x93,
        0x94,
        0x95,
        0x96,
        0x97,
        0x98,
        0x99,
        0x9A,
        0xA2,
        0xA3,
        0xA4,
        0xA5,
        0xA6,
        0xA7,
        0xA8,
        0xA9,
        0xAA,
        0xB2,
        0xB3,
        0xB4,
        0xB5,
        0xB6,
        0xB7,
        0xB8,
        0xB9,
        0xBA,
        0xC2,
        0xC3,
        0xC4,
        0xC5,
        0xC6,
        0xC7,
        0xC8,
        0xC9,
        0xCA,
        0xD2,
        0xD3,
        0xD4,
        0xD5,
        0xD6,
        0xD7,
        0xD8,
        0xD9,
        0xDA,
        0xE1,
        0xE2,
        0xE3,
        0xE4,
        0xE5,
        0xE6,
        0xE7,
        0xE8,
        0xE9,
        0xEA,
        0xF1,
        0xF2,
        0xF3,
        0xF4,
        0xF5,
        0xF6,
        0xF7,
        0xF8,
        0xF9,
        0xFA,
        0xFF,
        0xC4,
        0x00,
        0xB5,
        0x11,
        0x00,
        0x02,
        0x01,
        0x02,
        0x04,
        0x04,
        0x03,
        0x04,
        0x07,
        0x05,
        0x04,
        0x04,
        0x00,
        0x01,
        0x02,
        0x77,
        0x00,
        0x01,
        0x02,
        0x03,
        0x11,
        0x04,
        0x05,
        0x21,
        0x31,
        0x06,
        0x12,
        0x41,
        0x51,
        0x07,
        0x61,
        0x71,
        0x13,
        0x22,
        0x32,
        0x81,
        0x08,
        0x14,
        0x42,
        0x91,
        0xA1,
        0xB1,
        0xC1,
        0x09,
        0x23,
        0x33,
        0x52,
        0xF0,
        0x15,
        0x62,
        0x72,
        0xD1,
        0x0A,
        0x16,
        0x24,
        0x34,
        0xE1,
        0x25,
        0xF1,
        0x17,
        0x18,
        0x19,
        0x1A,
        0x26,
        0x27,
        0x28,
        0x29,
        0x2A,
        0x35,
        0x36,
        0x37,
        0x38,
        0x39,
        0x3A,
        0x43,
        0x44,
        0x45,
        0x46,
        0x47,
        0x48,
        0x49,
        0x4A,
        0x53,
        0x54,
        0x55,
        0x56,
        0x57,
        0x58,
        0x59,
        0x5A,
        0x63,
        0x64,
        0x65,
        0x66,
        0x67,
        0x68,
        0x69,
        0x6A,
        0x73,
        0x74,
        0x75,
        0x76,
        0x77,
        0x78,
        0x79,
        0x7A,
        0x82,
        0x83,
        0x84,
        0x85,
        0x86,
        0x87,
        0x88,
        0x89,
        0x8A,
        0x92,
        0x93,
        0x94,
        0x95,
        0x96,
        0x97,
        0x98,
        0x99,
        0x9A,
        0xA2,
        0xA3,
        0xA4,
        0xA5,
        0xA6,
        0xA7,
        0xA8,
        0xA9,
        0xAA,
        0xB2,
        0xB3,
        0xB4,
        0xB5,
        0xB6,
        0xB7,
        0xB8,
        0xB9,
        0xBA,
        0xC2,
        0xC3,
        0xC4,
        0xC5,
        0xC6,
        0xC7,
        0xC8,
        0xC9,
        0xCA,
        0xD2,
        0xD3,
        0xD4,
        0xD5,
        0xD6,
        0xD7,
        0xD8,
        0xD9,
        0xDA,
        0xE2,
        0xE3,
        0xE4,
        0xE5,
        0xE6,
        0xE7,
        0xE8,
        0xE9,
        0xEA,
        0xF2,
        0xF3,
        0xF4,
        0xF5,
        0xF6,
        0xF7,
        0xF8,
        0xF9,
        0xFA,
        0xFF,
        0xDA,
        0x00,
        0x0C,
        0x03,
        0x01,
        0x00,
        0x02,
        0x11,
        0x03,
        0x11,
        0x00,
        0x3F,
        0x00,
    ]
)

image_buffer = b""
last_fps_time = time.time()
fps = 0


def receive_data(data):
    global image_buffer
    global last_fps_time
    global fps

    if len(data) == 1:
        with open("temp_focus_image.jpg", "wb") as f:
            f.write(header + image_buffer)
            image_buffer = b""
            fps = 1 / (time.time() - last_fps_time)
            last_fps_time = time.time()
        return

    image_buffer += data[1:]
    print(
        f"\rReceived {str(len(image_buffer)-1)} bytes. FPS = {fps}. Press enter to finish      ",
        end="",
    )


async def main():
    # Connect to bluetooth
    b = Bluetooth()
    print("Connect Bluetooth")
    
    lua_script = """
    while false do
    end
    """
    
    await b.connect(
        # print_response_handler=lambda s: print("\r" + s, end=""),
        data_response_handler=receive_data,
    )
    await b.upload_file(lua_script, "main.lua")

    print("Send reset")
    await b.send_reset_signal()
    
    async def rr(a):
        time.sleep(0.005)
        r = await b.send_lua(f'print(string.byte(frame.fpga_read(0x{a:02X}, 1), 1))', await_print=True)
        return int(r)
        
    async def rr_(a):
        r = await rr(a)
        print(hex(a), hex(r))
        return r
      
    async def rr2(a):
        time.sleep(0.005)
        r0 = await b.send_lua(f'print(string.byte(frame.fpga_read(0x{a:02X}, 1), 1))', await_print=True)
        time.sleep(0.005)
        r1 = await b.send_lua(f'print(string.byte(frame.fpga_read(0x{a:02X}, 2), 2))', await_print=True)
        return 256*int(r1)+int(r0)
        
    async def rr2_(a):
        r = await rr2(a)
        print(hex(a), hex(r))
        return r  

    async def rrN(a, n=9):
        time.sleep(0.005)
        r1 = []
        for i in range(n):
            r0 = await b.send_lua(f'print(string.byte(frame.fpga_read(0x{a:02X}, {n}), {i+1}))', await_print=True)
            r0 = int(r0)
            r1.append(r0)
            time.sleep(0.005)
        return r1

    async def rrN_(a, n=9):
        r_ = await rrN(a, n)
        print('*r_=', r_, hex(a), [hex(s) for s in r_])
        return r_

    # Read ID
    print("Read ID")
    await rr_(0xdb)

    # Check PLL lock flag
    print("Check PLL lock flag")
    while True:
        lock = await rr_(0x41)
        if lock:
            break

    # Display buffer
    old_buf = await rr_(0x18)
    old_buf = int(old_buf)

    print("Switch Display buffer")
    await b.send_lua(f'frame.fpga_write(0x14, 1)')
    time.sleep(0.005)

    old_buf = await rr_(0x18)
    old_buf = await rr_(0x18)
    time.sleep(3)

    # Animation 16x16 bloxk
    width = 16
    y_pos = 50
    for i in range(400):
        x_pos = 50 + (15*i + 50)%400
        s = [x_pos>>8, x_pos & 0xff, y_pos>>8, y_pos & 0xff, width>>8, width & 0xff, 2, 0] + [0xff]*32
        s = ''.join([f"\\{j}" for j in s])
        cmd = f"frame.fpga_write(0x12, \"{s}\")"
        #print('CMD = ', cmd)

        #r_ = await rrN_(0x19)
        #print(hex(0x19), r_)
            
        timeout = 0
        while True:
            await b.send_lua(cmd)
            time.sleep(0.001)  

            old_buf = await rr(0x18)
            old_buf = int(old_buf)
            time.sleep(0.001)

            print(f"Switch Display buffer {1 - old_buf}")
            await b.send_lua(f'frame.fpga_write(0x14, 1)')
            time.sleep(0.001)
            
            buf = await rr(0x18)
            buf = int(buf)

            time.sleep(0.001)
            if buf != old_buf and int(buf) in [0,1]:
                old_buf = buf
                break
            print(f'---------------------     {buf}')
            if  timeout > 5:
                break
            timeout += 1

    # Wait until a keypress
    print("Wait until a keypress")
    await ainput("")


    await b.upload_file(lua_script, "main.lua")
    print("Send reset")
    await b.send_reset_signal()

    # Wait until a keypress
    print("Wait until a keypress")
    await ainput("")

    await b.send_break_signal()
    await b.disconnect()


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
