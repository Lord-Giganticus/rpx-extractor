# rpx-extractor
A python script to extract rpx files from Wii U titles

## Usage:
`python -3 rpx-extractor.py`

## Python Requirements:
cryptography

## Notes:
- There are two ways to get rpx files from titles, getting it from the WUP format or from the Loadiine format
- WUP format is used to install titles which can be gained by using [disc2app](https://github.com/koolkdev/disc2app)
- Loadiine format is the extracted form of WUP and is used in `\storage_mlc` by the Wii U. This can be gained by using [ddd](https://github.com/dimok789/ddd)
- You can also gain the Loadiine format from the WUP format by using [cdecrypt](https://github.com/phacoxcll/cdecrypt) or use [FTPiiU_Everywhere](https://github.com/FIX94/ftpiiu/) to dump it from sysNAND
- The python makes use of both ddd and cdecrypt in order to ensure you can get the rpx. It'll start by asking which fromat to get the rpx from.
- Due to potential risk, the wii u common key (`common key.txt`) has been encrypted using cryptography, the script will decode it during it's run. The key to decode it is in the `docs` folder of the repo.
