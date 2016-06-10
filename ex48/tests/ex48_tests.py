from nose.tools import *
from ex48.input_handle import lexicon

def test_dirctions():
    my_lexicon = lexicon()
    assert_equal(my_lexicon.scan("north"),[('direction','north')])
    result = my_lexicon.scan("north south east")
    assert_equal(result,[('direction','north'),
                         ('direction','south'),
                         ('direction','east')])
def test_verbs():
    my_lexicon = lexicon()
    assert_equal(my_lexicon.scan("go"),[('verb','go')])
    result = my_lexicon.scan("go kill eat")
    assert_equal(result,[('verb','go'),
                         ('verb','kill'),
                         ('verb','eat')])
def test_stops():
    my_lexicon = lexicon()
    assert_equal(my_lexicon.scan("The"),[('stop','the')])
    result = my_lexicon.scan("the in of")
    assert_equal(result,[('stop','the'),
                         ('stop','in'),
                         ('stop','of')])
def test_nouns():
    my_lexicon = lexicon()
    assert_equal(my_lexicon.scan("bear"),[('noun','bear')])
    result = my_lexicon.scan("bear princess")
    assert_equal(result,[('noun','bear'),
                         ('noun','princess')])

def test_numbers():
    my_lexicon = lexicon()
    assert_equal(my_lexicon.scan("1234"),[('number','1234')])
    result = my_lexicon.scan("3 91234")
    assert_equal(result,[('number','3'),
                         ('number','91234')])

def test_errors():
    my_lexicon = lexicon()
    assert_equal(my_lexicon.scan("ASDFS"),[('error','ASDFS')])
    result = my_lexicon.scan("bear IAS princess")
    assert_equal(result,[('noun','bear'),
                         ('error','IAS'),
                         ('noun','princess')])
