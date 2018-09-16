# -*- coding: UTF-8 -*-

class MemFormat:
    line_bytes = 16             #每行显示字节数
    line_space_split_bytes = 4  #相隔多少个字节显示空格

    def __init__(self, line_bytes = 16, split_bytes = 4):
        self.line_bytes = line_bytes
        self.line_space_split_bytes = split_bytes

    	

# 字节流就是字节数组
# 字符转数字ord(x)    => 'a'(str) -> 97 (int)
# 数字转字符chr(x)    => 97 (int) -> 'a'(str)
# 显示转字符串 str(x) => 97 (int) -> '97'(str)

    


    #字节流转显示的流文本，譬如 979797(长度3) ->'616161' (16进制，长度是6)
    def stream_to_text(self, s): 
        x = ''
        for _ in s:
            x = x + ('0' + hex(ord(_))[2:])[-2:]
        return x
    
    #流转可见的ascii码， 譬如00009798   -> ..aa   (不可见输出.)
    def stream_to_visible_ascii(self, s):
        x = ''
        for _ in s:
            if ord(_) >= 32 and ord(_) <= 126:
                x = x + _
            else:
                x = x + '.'
        return x
   

    def format(self, s):
        result = []
        
        split_str = [s[_:_+self.line_bytes] for _ in range(0, len(s), self.line_bytes)]
        for line_str in split_str:
            text = self.stream_to_text(line_str)
            visible = self.stream_to_visible_ascii(line_str)
            
            text = [text[_:_+self.line_space_split_bytes*2] for _ in range(0, len(text), self.line_space_split_bytes*2)]
            text = ' '.join(text)

            #visible = [visible[_:_+self.line_space_split_bytes] for _ in range(0, len(visible), self.line_space_split_bytes)]
            #visible = ' '.join(visible)
            visible = visible.ljust(self.line_bytes, '.')

            result.append(text.ljust(self.line_bytes*2 + self.line_bytes/self.line_space_split_bytes + 8) + visible)

        return '\n'.join(result)           
	

 



if __name__ == '__main__':
    print 'test...'
    x = [0,1,2,3,4,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    s = [chr(_) for _ in x]
    s = ''.join(s)
    print MemFormat().format(s)
