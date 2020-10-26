class vs module

class Practice 
  def self.foo
    something  
  end

  def self.bar
    something
  end
end

self.foo와 같이 self가 붙은것을 클래스 메소드라 명시
클래스 메소드만 가지는 클래스는 모듈로 뺀다

module Practice
  module_function
  def foo
    something
  end

  def bar
    something
  end
end

module_function은 
module에서 인스턴스 메소드를 클래스 메소드로 바꿀 때 사용
(self 명령어를 뺄수 있게 해준다)