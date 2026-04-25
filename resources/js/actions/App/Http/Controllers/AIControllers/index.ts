import AIController from './AIController'
import ChatController from './ChatController'
const AIControllers = {
    AIController: Object.assign(AIController, AIController),
ChatController: Object.assign(ChatController, ChatController),
}

export default AIControllers