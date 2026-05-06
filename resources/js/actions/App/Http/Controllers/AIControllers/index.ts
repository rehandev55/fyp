import AIController from './AIController'
import QuizController from './QuizController'
import ChatController from './ChatController'
const AIControllers = {
    AIController: Object.assign(AIController, AIController),
QuizController: Object.assign(QuizController, QuizController),
ChatController: Object.assign(ChatController, ChatController),
}

export default AIControllers