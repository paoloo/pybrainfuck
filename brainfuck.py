def bfrun(_PROG):
  MEMORIA = 1024
  _code = filter(lambda _c: _c in ['.', ',', '[', ']', '<', '>', '+', '-'],_PROG)
  _tmp,_l_block=[],{}
  for _i,_c in enumerate(_code):
    if _c == '[': _tmp.append(_i)                       # BRAINFUCK INTERPRETER
    if _c == ']':
      _m = _tmp.pop()
      _l_block[_m]=_i                                   # operacoes em C
      _l_block[_i]=_m                                   # --------------
  _pilha=[0]*MEMORIA                                    # char array[MEMORIA] = {0};
  pos, atual, offset = 0,0,0                            # char *ptr=array;
  while offset < len(_code):
    _c = _code[offset]
    if _c == '':                                        # --------------
      pass
    elif _c == '>':                                     # ++ptr;
      pos = pos + 1 if pos < MEMORIA else pos
    elif _c == '<':                                     # --ptr;
      pos = pos - 1 if pos > 0 else pos
    elif _c == '+':                                     # ++*ptr;
      _pilha[pos] = 0 if _pilha[pos] == 255 else _pilha[pos]+1        
    elif _c == '-':                                     # --*ptr;
      _pilha[pos] = 255 if _pilha[pos] == 0 else _pilha[pos]-1
    elif _c == '.':                                     # putchar(*ptr);
      __import__("sys").stdout.write('%c' % chr(_pilha[pos]))
    elif _c == ',':                                     # *ptr=getchar();
      _pilha[pos] = __import__("os").read(0,1)
    elif _c == '[':                                     # while (*ptr) {
      offset = _l_block[offset] if _pilha[pos] == 0 else offset
    elif _c == ']':                                     # }
      offset = _l_block[offset] if _pilha[pos] != 0 else offset
    else:
      pass
    offset+=1