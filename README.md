# rpx-extractor
A python script to extract rpx files from Wii U titles

## Usage:
`python -3 rpx-extractor.py`

## Python Requirements:
cryptography

## Windows Requirements:
curl installed to PATH

## Notes:
- There are two ways to get rpx files from titles, getting it from the WUP format or from the Loadiine format
- WUP format is used to install titles which can be gained by using [disc2app](https://github.com/koolkdev/disc2app)
- Loadiine format is the extracted form of WUP and is used in `\storage_mlc` by the Wii U. This can be gained by using [DDD](https://github.com/dimok789/ddd)
- You can also gain the Loadiine format from the WUP format by using [CDecrypt](https://github.com/phacoxcll/cdecrypt) or use [FTPiiU_Everywhere](https://github.com/FIX94/ftpiiu/) to dump it from sysNAND
- It is also possible to gain the Loadinne format by using [Dumpling](https://github.com/emiyl/dumpling)
- The python script makes use of DDD, CDecrypt, FTPiiU_Everywhere, and a Dumpling dump in order to ensure you can get the rpx. It'll start by asking which fromat to get the rpx from.
- Due to potential risk, the wii u common key (`core/common_key.txt`) has been encrypted using cryptography, the script will decode it during it's run. The key to decode it is in the `core` folder of the repo.
