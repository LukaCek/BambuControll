G1 X1
G1 Z0.8 F4000
G1 Y0
G1 Y251

G1 X50
G1 Z0.8
G1 Y0
G1 Y251

G1 X100
G1 Z0.8
G1 Y0
G1 Y251

G1 X150
G1 Z0.8
G1 Y0
G1 Y251

G1 X256
G1 Z0.8
G1 Y0
G1 Y251

G1 X206
G1 Z0.8
G1 Y0
G1 Y251

G1 X150
G1 Z0.8
G1 Y0
G1 Y251

G1 X100
G1 Z0.8
G1 Y0
G1 Y251

G1 Z50 F1000

M220 S100  ; Reset feedrate magnitude
M201.2 K1.0 ; Reset acc magnitude
M73.2   R1.0 ;Reset left time magnitude
M1002 set_gcode_claim_speed_level : 0

M17 X0.8 Y0.8 Z0.5 ; lower motor current to 45% power