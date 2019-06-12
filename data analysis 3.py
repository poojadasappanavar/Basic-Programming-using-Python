class Talk:
    def __init__(self,speaker,title,tags):
        self.speaker=speaker
        self.title=title
        self.tags=tags
        
    def get_speaker_firstname(self):
        return self.speaker.split()[0]
        
    def get_tags(self):
        return self.tags.split(',')
        

bdfl=Talk('Guido van Rossum','The history python','python,history,C,advanced')

bdfl
Out[87]: <__main__.Talk at 0x2173aa6e860>

type(bdfl)
Out[88]: __main__.Talk

bdfl.get_speaker_firstname()
Out[89]: 'Guido'

bdfl.get_tags()
Out[90]: ['python', 'history', 'C', 'advanced']

bdfl.title
Out[91]: 'The history python'

talk.speaker='Arun K B' 

talk.tags='python,biopython'

talk.get_tags()
Out[97]: ['python', 'biopython']