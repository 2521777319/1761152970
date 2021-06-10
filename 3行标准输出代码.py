#这玩意有时候能用有时候不能用自己慢慢试吧
#主要使用的还是req.encoding = 'utf-8'
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'gb18030')
