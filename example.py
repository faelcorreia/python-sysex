#!/usr/bin/env python3

from sysex import SysEx
import rtmidi
import traceback
import time

def main():
    midiout = rtmidi.MidiOut()
    ports = midiout.get_ports()
    if ports:
        detected = -1
        for i, port in enumerate(ports):
            if port[:6] == "XPS-10":
                detected = i
        if i > -1:
            print("XPS-10 detected.")
            try:
                midiout.open_port(i)
                sysex = SysEx("impl/xps10.json")
                print("Initializing patch (hacked from Juno Di)...")
                midiout.send_message(sysex.generate_message(
                    "PATCH_COMMON", "505954484F4E2D535953455800007F4000404040000001000000000000140007080040404040400D00020262094A00400040004063044002400040004064044002400040004065044002400040004000"))
                time.sleep(0.02)
                midiout.send_message(sysex.generate_message(
                    "PATCH_COMMON_MFX", "007F0000000040004000400040000000000800060408000604080000000800070F080000010800010508000000080001080800000C08000001080000000800000F080000070800000F08000000080000010800000F0800070F08000102080006040800060408000302080000000800000008000102080003010800000F0800000F080006040800070F0800000008000000"))
                time.sleep(0.02)
                midiout.send_message(sysex.generate_message(
                    "PATCH_COMMON_CHORUS", "007F000008000000080004000800000808000500080000030800010308000000080000000800000C0800030B080001010800070F0800070F0800070F080000000800000008000000080000000800000008000000"))
                time.sleep(0.02)
                midiout.send_message(sysex.generate_message(
                    "PATCH_COMMON_REVERB", "007F0008000004080000000800040008000400080000000800070F0800010308000204080000000800020408000000080000000800000008000000080000000800000008000000080000000800000008000000"))
                time.sleep(0.02)
                midiout.send_message(sysex.generate_message(
                    "PATCH_TMT", "000000000101007F0000017F000000007F0000017F000000007F0000017F000000007F0000017F0000"))
                time.sleep(0.02)
                midiout.send_message(sysex.generate_message(
                    "PATCH_TONE_1", "7F40400040400040010000007F00007F7F000101010000010101010101010101010101010101010000000001000000010000000001000000004A40404040402850280040225E4040017F4001400040400140404040000A0A40007F7F7F00403C030160404040000A0A0A7F7F7F01050C020000400000004040404001050C02000040000000404040400040404040404040404040404040404040"))
                time.sleep(0.02)
                midiout.send_message(sysex.generate_message(
                    "PATCH_TONE_2", "7F40400040400040010000007F00007F7F000101010000010101010101010101010101010101010000000001000000010000000001000000004A40404040402850280040225E4040017F4001400040400140404040000A0A40007F7F7F00403C030160404040000A0A0A7F7F7F01050C020000400000004040404001050C02000040000000404040400040404040404040404040404040404040"))
                time.sleep(0.02)
                midiout.send_message(sysex.generate_message(
                    "PATCH_TONE_3", "7F40400040400040010000007F00007F7F000101010000010101010101010101010101010101010000000001000000010000000001000000004A40404040402850280040225E4040017F4001400040400140404040000A0A40007F7F7F00403C030160404040000A0A0A7F7F7F01050C020000400000004040404001050C02000040000000404040400040404040404040404040404040404040"))
                midiout.send_message(sysex.generate_message(
                    "PATCH_TONE_4", "7F40400040400040010000007F00007F7F000101010000010101010101010101010101010101010000000001000000010000000001000000004A40404040402850280040225E4040017F4001400040400140404040000A0A40007F7F7F00403C030160404040000A0A0A7F7F7F01050C020000400000004040404001050C02000040000000404040400040404040404040404040404040404040"))
                time.sleep(0.02)

                print("Setting patch to mono...")
                midiout.send_message(sysex.generate_message(
                    "PATCH_COMMON_MONO_POLY", "00"))
                time.sleep(0.02)

                print("Selecting sawtooth wave to tone 1...")
                midiout.send_message(sysex.generate_message(
                    "PATCH_WAVE_NUMBER_L", "00010E09"))
                time.sleep(0.02)

                print("Turning off TVA velocity from tone 1...")
                midiout.send_message(sysex.generate_message(
                    "PATCH_TONE_1_TVA_LEVEL_VELOCITY_SENS", "40"))

            except rtmidi._rtmidi.SystemError:
                print("Not possible to open port. Are you using another MIDI software?")
            except Exception:
                traceback.print_exc()
        else:
            print("XPS-10 not detected.")
    else:
        print("No MIDI ports found.")


if __name__ == "__main__":
    main()
