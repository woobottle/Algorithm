%w -> 단어에 대한 배열이 필요할때 선언

# 나쁜 예
STATES = ['draft', 'open', 'closed']

# 좋은 예
STATES = %w[draft open closed]

%i -> 심볼에 대한 배열이 필요할때 선언

# 나쁜 예
STATES = [:draft, :open, :closed]

# 좋은 예
STATES = %i[draft open closed]