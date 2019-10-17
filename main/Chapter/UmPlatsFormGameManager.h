
#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

@interface UmPlatsFormGameManager : NSObject

///**
// * 单例方法
// 
// @return 返回 UmPlatFormGameManager 对象
// */
+(instancetype)umPlatsFormManagerDeafaults;

#pragma mark ---------- 在登录页面显示前插入视频
/**
 在游戏开始前插入视频 (亦可在bundle中设置对应的值)

 @param videoName 视频的名称
 @param videoType 视频的类型（例如：mp4  mov）
 @param present 根据视频长度比例取值显示跳过按钮（例如10秒视频，那么如果present = 0.3，那么就是3秒后显示）
 @param block 视频播放完成后的回调
 */
-(void)umPlatsFormPlayVideo:(NSString *)videoName
                  videoType:(NSString *)videoType
           passVideoPresent:(CGFloat)present
                 finishPlay:(void(^)(void))block;

#pragma mark ---------- 停止播放视频
-(void)umPlatsFormStopPlayVideo;


#pragma mark ---------- 登录入口
/**
 * SDK 登录入口
 */
-(void)umPlatsFormLogin;

#pragma mark ---------- 注销，切换账号，需要再次调用登录入口
/**
 * SDK 注销
 * 在登录状态下，需要重新弹出 SDK 界面的都需要先调用注销接口。先移除登录状态
 */
-(void)umPlatsFormLogout;

#pragma mark ---------- 充值
/**
 * 充值接口
 
 @param productId       苹果产品Id
 @param money           金额（元）
 @param cpOrderId       cp订单号Id
 @param ProductName     商品名字
 @param description     商品描述
 @param roleId          角色ID
 @param roleName        角色名字
 @param roleLevel       角色等级
 @param serverId        服务器ID
 @param serverName      服务器名字
 @param memo            透传参数
 */

-(void)umPlatsFormProductId:(NSString*)productId
            withAppleMoney:(NSString*)money
             withCpOrderId:(NSString*)cpOrderId
           WithProductName:(NSString*)ProductName
           withProductDesc:(NSString*)description
                withRoleId:(NSString*)roleId
              withRoleName:(NSString*)roleName
             withRoleLevel:(NSString*)roleLevel
              withServerID:(NSString*)serverId
            withServerName:(NSString*)serverName
                  withMemo:(NSString*)memo;

#pragma mark ---------- 数据上报

/**
 * 角色创建、登录与升级时，调用此接口
 @param upType          接口类型 （1 == 创建角色 2 == 角色登录 3 == 角色升级）
 @param roleName        角色名字
 @param roleId          角色ID
 @param roleLevel       角色等级
 @param serverId        服务器ID
 @param serverName      服务器名字
 @param vipLevel        VIP等级
 @param coin            金币数量
 */
-(void)umPlatsFormUploadRoleInfoType:(int)upType
                       WithRoleName:(NSString*)roleName
                         withRoleId:(NSString*)roleId
                      withRoleLevel:(NSString*)roleLevel
                       withServerId:(NSString*)serverId
                     withServerName:(NSString*)serverName
                       withVipLevel:(NSString*)vipLevel
                       withGameCoin:(NSString*)coin;

#pragma mark ---------- 应用配置

/**
 * SDK 基本信息配置接口
 * 需要在启动函数里调用 - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
 
 ********** 由于激活统计需要，请务必把该接口放置所有接口之前。启动即调用。
 @param gid       字符串   游戏id
 @param sub_gid   字符串   游戏子包id
 */

-(void)umPlatsFormLaunchConfigGameID:(NSString *)gid WithSub_GameID:(NSString *)sub_gid;
/**
 * SDK 返回应用设置
 * 需要返回应用接口调用 - (void)applicationWillEnterForeground:(UIApplication *)application
 
 */
-(void)umPlatsFormApplicationWillEnterForeground;

@end
