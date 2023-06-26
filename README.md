## 에버노트 텍스트 암호화/복호화 스크립트

- 에버노트 내부 기능인 텍스트 암호화/복호화기능을 따로 구현한 스크립트입니다.

- Joplin이나 노션등 다른 노트로 에버노트를 옮길경우 암호화된 텍스트는 복호화되지않고, 암호화된 텍스트로 export되는데 이 경우 해당부분만 복호화 할수있도록 만든 스크립트입니다. 

- 물론 비밀번호가 매칭되어야 복호화가 가능합니다.

- 에버노트가 사용하는 방식으로 암호화하려면 Evernote_Encrypt 스크립트를 사용하면 됩니다. 
- 참고한 [사이트 링크 및 스크립트](https://soundly.me/decoding-the-Evernote-en-crypt-field-payload/)는 다음과 같으며, 가볍게 사용할수있도록 살짝 수정만하였습니다. 



### 실행방법

> python Evernote_Decrypt.py 

실행후 패스워드를 입력하고 복호화를 원하는 텍스트를 입력하면 됩니다. (얌호화 역시 동일합니다.)

피드백 및 문의, fork 언제나 환영합니다 :)


<br>
<br>

---



## Evernote Text Encryption/Decryption Script

- This script is a separate implementation of the text encryption/decryption feature found in Evernote.
- When migrating Evernote to other note-taking apps like Joplin or Notion, encrypted text does not get decrypted and is exported as encrypted text. This script allows for decrypting only the specific parts that were encrypted.
- Of course, the decryption is only possible if the passwords match.
- To encrypt text in the same way Evernote does, you can use the Evernote_Encrypt script. 

- The script referenced in the site [link](https://soundly.me/decoding-the-Evernote-en-crypt-field-payload/) and script was slightly modified for ease of use.

### Execution
> python Evernote_Decrypt.py

After executing the script, enter the password and the text you want to decrypt. (Encryption works the same way.)


Feedback, inquiries, and forks are always welcome :)