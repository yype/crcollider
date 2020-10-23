from crcollider import collcrc
from crc_funcs import crc64, crc32

def crc96(m):
    return (crc32(m) << 64) + crc64(m)

def solve_chal():
    with open('example/example.bmp', 'rb') as f:
        org_img = f.read()

    rg = list(range(len(org_img)*8))
    available_bits = []
    for i in range(12):
        available_bits += rg[54*8+i*8:54*8+(i+1)*8]

    sol_num, sols = collcrc(crc96, 96, org_img, available_bits, 0x0)
    
    print(f'{sol_num} solution(s) found')

    for i, each in enumerate(sols):
        file_out = f'example/example_faked_{i}.bmp'
        print(f'Outputting sol{i} to {file_out}...')
        with open(file_out, 'wb') as f:
            f.write(each)

if __name__ == '__main__':
    solve_chal()
