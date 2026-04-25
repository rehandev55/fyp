import Api from './Api'
import AIControllers from './AIControllers'
import Admin from './Admin'
import DashboardController from './DashboardController'
import SelectionController from './SelectionController'
import AiChatController from './AiChatController'
import PracticeController from './PracticeController'
import ResourceController from './ResourceController'
import ProgressController from './ProgressController'
import ProfileController from './ProfileController'
import AboutController from './AboutController'
import Settings from './Settings'
const Controllers = {
    Api: Object.assign(Api, Api),
AIControllers: Object.assign(AIControllers, AIControllers),
Admin: Object.assign(Admin, Admin),
DashboardController: Object.assign(DashboardController, DashboardController),
SelectionController: Object.assign(SelectionController, SelectionController),
AiChatController: Object.assign(AiChatController, AiChatController),
PracticeController: Object.assign(PracticeController, PracticeController),
ResourceController: Object.assign(ResourceController, ResourceController),
ProgressController: Object.assign(ProgressController, ProgressController),
ProfileController: Object.assign(ProfileController, ProfileController),
AboutController: Object.assign(AboutController, AboutController),
Settings: Object.assign(Settings, Settings),
}

export default Controllers