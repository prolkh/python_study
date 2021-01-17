# import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

### debug < info < waring < error < critical
# logging.debug("디버그")
# logging.info("인포메이션")
# logging.warning("경고")
# logging.error("에러")
# logging.critical("심각한 문제")

### 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime

# 시간 [로그레벨] 메시지 형태로 로그를 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

#파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile20212059000000.log
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남기는 테스트를 해보다.")