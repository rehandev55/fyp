import AIController from './AIController'
import DashboardController from './DashboardController'
import SelectionController from './SelectionController'
import AiChatController from './AiChatController'
import PracticeController from './PracticeController'
import ResourceController from './ResourceController'
import ProgressController from './ProgressController'
import ProfileController from './ProfileController'
import AboutController from './AboutController'
import Admin from './Admin'
import Settings from './Settings'
const Controllers = {
    AIController: Object.assign(AIController, AIController),
DashboardController: Object.assign(DashboardController, DashboardController),
SelectionController: Object.assign(SelectionController, SelectionController),
AiChatController: Object.assign(AiChatController, AiChatController),
PracticeController: Object.assign(PracticeController, PracticeController),
ResourceController: Object.assign(ResourceController, ResourceController),
ProgressController: Object.assign(ProgressController, ProgressController),
ProfileController: Object.assign(ProfileController, ProfileController),
AboutController: Object.assign(AboutController, AboutController),
Admin: Object.assign(Admin, Admin),
Settings: Object.assign(Settings, Settings),
}

export default Controllers