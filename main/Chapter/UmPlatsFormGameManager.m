
#import "UmPlatsFormGameManager.h"
#import "ClassNames_ModelFactory.h"
#import "ClassNames_DeviceConfig.h"
#import "ClassNames_ThemeConfig.h"
#import "ClassNames_NotificationConfigure.h"
#import "ClassNames_ViewModelFactory.h"
#import "ClassNames_EnumHeader.h"
#import "ClassNames_ViewFactory.h"
#import "ClassNames_MainView.h"
#import "ClassNames_SuspensionBallButton.h"
#import "ClassNames_PGHubView.h"
#import "ClassNames_RechargeView.h"
#import "ClassNames_VideoPlayView.h"
#import "ClassNames_IAPPayManager.h"
#import "ClassNames_IAPReplenishmentManager.h"
#import "ClassNames_LanguageFactorManager.h"
#import "ClassNames_CustomServerView.h"
@interface UmPlatsFormGameManager ()

#pragma mark ---------- 语言
@property (nonatomic, readwrite, strong) ClassNames_BaseLanguageContent *varNames_languageContent;

#pragma mark ---------- 初始化
@property (nonatomic, readwrite, strong) ClassNames_GameInitialiseModel *varNames_gameInitModel;
#pragma mark ---------- 设备激活
@property (nonatomic, readwrite, strong) ClassNames_ActivateModel *varNames_activateModel;

@property (nonatomic, readwrite, strong) ClassNames_MainView *varNames_mainView;

#pragma mark ---------- 上报登录信息，角色信息
@property (nonatomic, readwrite, strong) ClassNames_MembeRoleModel *varNames_uploadMemberRoleModel;
@property (nonatomic, readwrite, strong) ClassNames_UpdateUserLoginModel *varNames_uploadLoginModel;


@property (nonatomic, readwrite, strong) ClassNames_VideoPlayView *varNames_videoPlayView;

@property (nonatomic, readwrite, strong) ClassNames_SuspensionBallButton *varNames_suspensionBall;
@property (nonatomic, readwrite, strong) ClassNames_QQServerModel *varNames_qqserverModel;
@property (nonatomic, readwrite, strong) ClassNames_WalkThroughModel *varNames_walkthroughModel;

#pragma mark ---------- 充值
@property (nonatomic, readwrite, strong) ClassNames_MemberOrderModel *varNames_orderModel;


#pragma mark ---------- 保存是否进行初始化操作流程
@property (nonatomic, readwrite, assign) BOOL varNames_isInit;
#pragma mark ---------- 初始化
@property (nonatomic, readwrite, strong) ClassNames_GameInitialiseModel *varNames_beforeLoginInitModel;
@end

@implementation UmPlatsFormGameManager

+(instancetype)umPlatsFormManagerDeafaults {
    static UmPlatsFormGameManager *varNames_umPlatsForm = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        varNames_umPlatsForm = [[UmPlatsFormGameManager alloc]init];
        [[NSNotificationCenter defaultCenter] addObserver:varNames_umPlatsForm selector:@selector(methodNames_loginNoti:) name:methodNames_getLoginFinishNotiName() object:nil];
    });
    return varNames_umPlatsForm;
}


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
                 finishPlay:(void(^)(void))block {
    
    NSString *varNames_videoNames = methodNames_getVideoName();
    NSString *varNames_videoType = methodNames_getVideoType();
    CGFloat varNames_passVideoPresent = methodNames_getPassVideoPresent();
    if (videoName && videoName.length) {
        varNames_videoNames = videoName;
    }
    if (videoType && videoType.length) {
        varNames_videoType = videoType;
    }
    if (present) {
        varNames_passVideoPresent = present;
    }
    self.varNames_videoPlayView = [ClassNames_VideoPlayView methodNames_showVideoWithVideoName:varNames_videoNames methodNames_videoType:varNames_videoType methodNames_showPassButton:varNames_passVideoPresent methodNames_finishPlay:block];
}

#pragma mark ---------- 停止播放视频
-(void)umPlatsFormStopPlayVideo {
    if (self.varNames_videoPlayView) {
        [self.varNames_videoPlayView methodNames_stopPlayer];
    }
}


#pragma mark ---------- 登录入口
/**
 * SDK 登录入口
 */
-(void)umPlatsFormLogin {
    
    [self methodNames_beforeLoginDoInitGameAction:^(BOOL varNames_argResult) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [ClassNames_PGHubView methodNames_hide];
            if (methodNames_readAppleCheck()) {
                if ([methodNames_getIsPassLogin() isEqualToString:methodNames_getStringOne()]) {
                    methodNames_debugLog(@"跳%……&*登^$@^%#录");
                    
                    if (!methodNames_getUid().length || !methodNames_getUserName().length) {
                        methodNames_debugLog(@"plist中没有设置uid和username得值");
                    } else {
                        methodNames_saveUserID(methodNames_getUid());
                        methodNames_saveUserName(methodNames_getUserName());
                        NSDictionary *varNames_tmpDic = @{
                                                          @"uid": methodNames_getUid(),
                                                          @"username": methodNames_getUserName(),
                                                          @"result": @"1"
                                                          };
                        methodNames_postLoginFinish(self, varNames_tmpDic);
                    }
                } else {
                    [self methodNames_loadLogin];
                }
            } else {
                [self methodNames_loadLogin];
            }
        });
    }];
}

#pragma mark ---------- 注销，切换账号，需要再次调用登录入口
/**
 * SDK 注销
 * 在登录状态下，需要重新弹出 SDK 界面的都需要先调用注销接口。先移除登录状态
 */
-(void)umPlatsFormLogout {
    methodNames_postLogoutFinish(self, @{@"result": @"1", @"msg": @"logoutSuccess"});
    methodNames_saveLastAccount(@"");
    if (self.varNames_suspensionBall) {
        [self.varNames_suspensionBall methodNames_hideSuspensionBall];
    }
    [self umPlatsFormLogin];
}

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
                   withMemo:(NSString*)memo {
    [self methodNames_ProductId:productId
      subMethodNames_AppleMoney:money
       subMethodNames_CpOrderId:cpOrderId
     subMethodNames_ProductName:ProductName
     subMethodNames_ProductDesc:description
          subMethodNames_RoleId:roleId
        subMethodNames_RoleName:roleName
       subMethodNames_RoleLevel:roleLevel
        subMethodNames_ServerID:serverId
      subMethodNames_ServerName:serverName
            subMethodNames_Memo:memo];
}

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
                        withGameCoin:(NSString*)coin {
    
    [self methodNames_uploadRoleInfoType:upType
                 subMethodNames_RoleName:roleName
                   subMethodNames_RoleId:roleId
                subMethodNames_RoleLevel:roleLevel
                 subMethodNames_ServerId:serverId
               subMethodNames_ServerName:serverName
                 subMethodNames_VipLevel:vipLevel
                 subMethodNames_GameCoin:coin];
}

#pragma mark ---------- 应用配置

/**
 * SDK 基本信息配置接口
 * 需要在启动函数里调用 - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
 
 ********** 由于激活统计需要，请务必把该接口放置所有接口之前。启动即调用。
 @param gid       字符串   游戏id
 @param sub_gid   字符串   游戏子包id
 */

-(void)umPlatsFormLaunchConfigGameID:(NSString *)gid WithSub_GameID:(NSString *)sub_gid {
    
    NSAssert(gid.length, @"gid 没有值");
    NSAssert(sub_gid.length, @"sub_gid 没有值");
    
    methodNames_saveGameID(gid);
    methodNames_saveSubGameID(sub_gid);
    
    NSString *varNames_tmpgid = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpsubgid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringu(), methodNames_getStringb(), methodNames_getStringUnderLine(), methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpgamever = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@", methodNames_getStringg(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr()];
    
    NSString *varNames_tmpdevicecode = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringv(), methodNames_getStringi(), methodNames_getStringc(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringc(), methodNames_getStringo(), methodNames_getStringd(), methodNames_getStringe()];
    
    
    NSMutableDictionary *varNames_tmpDic = [NSMutableDictionary dictionaryWithCapacity:3];
    [varNames_tmpDic setValue:gid forKey:varNames_tmpgid];
    [varNames_tmpDic setValue:sub_gid forKey:varNames_tmpsubgid];
    [varNames_tmpDic setValue:methodNames_getProjectVersion() forKey:varNames_tmpgamever];
    [varNames_tmpDic setValue:methodNames_getDeviceIDFA() forKey:varNames_tmpdevicecode];
    [self.varNames_gameInitModel methodNames_fetchDataWithParameters:varNames_tmpDic];
    __weak typeof(self) weakSelf = self;
    self.varNames_gameInitModel.varNames_fetchCompleteSuccess = ^(ClassNames_GameInitialiseModel *varNames_argObject) {
        if (![weakSelf methodNames_getGameInit]) {
            [weakSelf methodNames_setGameInit:YES];
            [weakSelf methodNames_dealWithSuccessInit:varNames_argObject];
        }
    };
    self.varNames_gameInitModel.varNames_fetchCompleteFailure = ^(NSString *varNames_argmessage) {
        [weakSelf methodNames_setGameInit:NO];
        [weakSelf methodNames_initFinishPostNotiWithResult:methodNames_getStringZero() subMethodNames_msg:varNames_argmessage];
        
    };
    self.varNames_gameInitModel.varNames_fetchError = ^(NSError *varNames_argError) {
        methodNames_debugLog(@"网络有问题");
        [weakSelf methodNames_setGameInit:NO];
        [weakSelf methodNames_initFinishPostNotiWithResult:methodNames_getStringZero() subMethodNames_msg:@"网络有问题"];
    };
    [self methodNames_activateDeviceWithGid:gid subMethodNames_subgid:sub_gid];
}
/**
 * SDK 返回应用设置
 * 需要返回应用接口调用 - (void)applicationWillEnterForeground:(UIApplication *)application
 */
-(void)umPlatsFormApplicationWillEnterForeground {
    methodNames_postPayFinish(self, @{});
    [self methodNames_stopReplenishAction];
}


#pragma mark ---------- privateMethod
#pragma mark ---------- 设置初始化的状态
- (void)methodNames_setGameInit:(BOOL)varNames_arginit {
    self.varNames_isInit = varNames_arginit;
}
- (BOOL)methodNames_getGameInit {
    return self.varNames_isInit;
}

#pragma mark ---------- 在显示登录前在进行一次判断是否初始化完成
- (void)methodNames_beforeLoginDoInitGameAction:(void(^)(BOOL varNames_argResult))varNames_argComplete {
    
    [ClassNames_PGHubView methodNames_showIndicator];
    
    if ([self methodNames_getGameInit]) {
        
        if (varNames_argComplete) {
            varNames_argComplete(YES);
        }
        return;
    }
    
    NSString *varNames_tmpgid = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpsubgid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringu(), methodNames_getStringb(), methodNames_getStringUnderLine(), methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpgamever = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@", methodNames_getStringg(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr()];
    
    NSMutableDictionary *varNames_tmpDic = [NSMutableDictionary dictionaryWithCapacity:3];
    [varNames_tmpDic setValue:methodNames_readGameID() forKey:varNames_tmpgid];
    [varNames_tmpDic setValue:methodNames_readSubGameID() forKey:varNames_tmpsubgid];
    [varNames_tmpDic setValue:methodNames_getProjectVersion() forKey:varNames_tmpgamever];
    __weak typeof(self) weakSelf = self;
    [self.varNames_beforeLoginInitModel methodNames_fetchDataWithParameters:varNames_tmpDic];
    self.varNames_beforeLoginInitModel.varNames_fetchCompleteSuccess = ^(ClassNames_GameInitialiseModel *varNames_argObject) {
        if (![weakSelf methodNames_getGameInit]) {
            [weakSelf methodNames_setGameInit:YES];
            [weakSelf methodNames_dealWithSuccessInit:varNames_argObject];
        }
        if (varNames_argComplete) {
            varNames_argComplete(YES);
        }
    };
    self.varNames_beforeLoginInitModel.varNames_fetchCompleteFailure = ^(NSString *varNames_argmessage) {
        [weakSelf methodNames_initFinishPostNotiWithResult:methodNames_getStringZero() subMethodNames_msg:varNames_argmessage];
        [weakSelf methodNames_setGameInit:NO];
        if (varNames_argComplete) {
            varNames_argComplete(NO);
        }
    };
    self.varNames_beforeLoginInitModel.varNames_fetchError = ^(NSError *varNames_argError) {
        methodNames_debugLog(@"网络有问题");
        [weakSelf methodNames_setGameInit:NO];
        [weakSelf methodNames_initFinishPostNotiWithResult:methodNames_getStringZero() subMethodNames_msg:@"网络有问题"];
        if (varNames_argComplete) {
            varNames_argComplete(NO);
        }
    };
}
#pragma mark ---------- 登录
- (void)methodNames_loadLogin {
    if (!self.varNames_mainView) {
        self.varNames_mainView = [ClassNames_MainView methodNames_showMainView];
    }
}


#pragma mark ---------- 数据上报
- (void)methodNames_uploadRoleInfoType:(int)varNames_argupType
               subMethodNames_RoleName:(NSString *)varNames_argroleName
                 subMethodNames_RoleId:(NSString *)varNames_argroleId
              subMethodNames_RoleLevel:(NSString *)varNames_argroleLevel
               subMethodNames_ServerId:(NSString *)varNames_argserverId
             subMethodNames_ServerName:(NSString *)varNames_argserverName
               subMethodNames_VipLevel:(NSString *)varNames_argvipLevel
               subMethodNames_GameCoin:(NSString *)varNames_argcoin {
    
    NSMutableDictionary *varNames_tmpDic = [NSMutableDictionary dictionary];
    
    NSString *varNames_tmpusername = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@", methodNames_getStringu(), methodNames_getStrings(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe()];
    NSString *varNames_tmpuid = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringu(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmproleid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStringr(), methodNames_getStringo(), methodNames_getStringl(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmprolename = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@", methodNames_getStringr(), methodNames_getStringo(), methodNames_getStringl(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe()];
    NSString *varNames_tmpplatformid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringp(), methodNames_getStringl(), methodNames_getStringa(), methodNames_getStringt(), methodNames_getStringf(), methodNames_getStringo(), methodNames_getStringr(), methodNames_getStringm(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpgid = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpsubgid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringu(), methodNames_getStringb(), methodNames_getStringUnderLine(), methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpgamegrade = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringg(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringg(), methodNames_getStringr(), methodNames_getStringa(), methodNames_getStringd(), methodNames_getStringe()];
    NSString *varNames_tmpchannelid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringc(), methodNames_getStringh(), methodNames_getStringa(), methodNames_getStringn(), methodNames_getStringn(), methodNames_getStringe(), methodNames_getStringl(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpcpserverid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringc(), methodNames_getStringp(), methodNames_getStringUnderLine(), methodNames_getStrings(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpvip = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringv(), methodNames_getStringi(), methodNames_getStringp()];
    NSString *varNames_tmpgamecoin = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@", methodNames_getStringg(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringc(), methodNames_getStringo(), methodNames_getStringi(), methodNames_getStringn()];
    NSString *varNames_tmpservername = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe()];
    NSString *varNames_tmplevel = [NSString stringWithFormat:@"%@%@%@%@%@", methodNames_getStringl(), methodNames_getStringe(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringl()];
    NSString *varNames_tmpadvid = [NSString stringWithFormat:@"%@%@%@%@%@%@", methodNames_getStringa(), methodNames_getStringd(), methodNames_getStringv(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    
    [varNames_tmpDic setValue:varNames_argroleId forKey:varNames_tmproleid];
    [varNames_tmpDic setValue:varNames_argroleName forKey:varNames_tmprolename];
    [varNames_tmpDic setValue:varNames_argroleLevel forKey:varNames_tmpgamegrade];
    [varNames_tmpDic setValue:varNames_argserverId forKey:varNames_tmpcpserverid];
    [varNames_tmpDic setValue:varNames_argvipLevel forKey:varNames_tmpvip];
    [varNames_tmpDic setValue:varNames_argroleLevel forKey:varNames_tmplevel];
    [varNames_tmpDic setValue:varNames_argserverName forKey:varNames_tmpservername];
    [varNames_tmpDic setValue:varNames_argcoin forKey:varNames_tmpgamecoin];
    
    [varNames_tmpDic setValue:methodNames_readUserName() forKey:varNames_tmpusername];
    [varNames_tmpDic setValue:methodNames_readUserID() forKey:varNames_tmpuid];
    [varNames_tmpDic setValue:methodNames_readPlatformID() forKey:varNames_tmpplatformid];
    [varNames_tmpDic setValue:methodNames_readGameID() forKey:varNames_tmpgid];
    [varNames_tmpDic setValue:methodNames_readSubGameID() forKey:varNames_tmpsubgid];
    [varNames_tmpDic setValue:methodNames_readChannelID() forKey:varNames_tmpchannelid];
    [varNames_tmpDic setValue:methodNames_readAdvID() forKey:varNames_tmpadvid];
    
    if (varNames_argupType == 2) {
        NSString *varNames_tmpsdkversion = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringd(), methodNames_getStringk(), methodNames_getStringUnderLine(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStrings(), methodNames_getStringi(), methodNames_getStringo(), methodNames_getStringn()];
        NSString *varNames_tmpdevicecode = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringv(), methodNames_getStringi(), methodNames_getStringc(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringc(), methodNames_getStringo(), methodNames_getStringd(), methodNames_getStringe()];
        NSString *varNames_tmpdevicebrand = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringv(), methodNames_getStringi(), methodNames_getStringc(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringb(), methodNames_getStringr(), methodNames_getStringa(), methodNames_getStringn(), methodNames_getStringd()];
        NSString *varNames_tmpmodeltype = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringm(), methodNames_getStringo(), methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringl(), methodNames_getStringUnderLine(), methodNames_getStringt(), methodNames_getStringy(), methodNames_getStringp(), methodNames_getStringe()];
        NSString *varNames_tmpdeviceresolution = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringv(), methodNames_getStringi(), methodNames_getStringc(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringr(), methodNames_getStringe(), methodNames_getStrings(), methodNames_getStringo(), methodNames_getStringl(), methodNames_getStringu(), methodNames_getStringt(), methodNames_getStringi(), methodNames_getStringo(), methodNames_getStringn()];
        NSString *varNames_tmpdevicenet = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringv(), methodNames_getStringi(), methodNames_getStringc(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringe(), methodNames_getStringt()];
        
        [varNames_tmpDic setValue:methodNames_getSDKVersion() forKey:varNames_tmpsdkversion];
        [varNames_tmpDic setValue:methodNames_getDeviceIDFA() forKey:varNames_tmpdevicecode];
        [varNames_tmpDic setValue:methodNames_getDeviceBrand() forKey:varNames_tmpdevicebrand];
        [varNames_tmpDic setValue:methodNames_getDeviceType() forKey:varNames_tmpmodeltype];
        [varNames_tmpDic setValue:methodNames_getDeviceResolution() forKey:varNames_tmpdeviceresolution];
        [varNames_tmpDic setValue:methodNames_getDeviceNetType() forKey:varNames_tmpdevicenet];
        
        [self.varNames_uploadLoginModel methodNames_fetchDataWithParameters:varNames_tmpDic];
        self.varNames_uploadLoginModel.varNames_fetchCompleteSuccess = ^(ClassNames_UpdateUserLoginModel *varNames_argObject) {
            methodNames_debugLog(varNames_argObject.varNames_msg);
        };
        self.varNames_uploadLoginModel.varNames_fetchCompleteFailure = ^(NSString *varNames_argmessage) {
            methodNames_debugLog(varNames_argmessage);
        };
    } else {
        [self.varNames_uploadMemberRoleModel methodNames_fetchDataWithParameters:varNames_tmpDic];
        self.varNames_uploadMemberRoleModel.varNames_fetchCompleteSuccess = ^(ClassNames_MembeRoleModel *varNames_argObject) {
            methodNames_debugLog(varNames_argObject.varNames_msg);
        };
        self.varNames_uploadMemberRoleModel.varNames_fetchCompleteFailure = ^(NSString *varNames_argmessage) {
            methodNames_debugLog(varNames_argmessage);
        };
        
        [self methodNames_startReplenishAction];
    }
}

#pragma mark ---------- 充值
-(void)methodNames_ProductId:(NSString*)varNames_argproductId
   subMethodNames_AppleMoney:(NSString*)varNames_argmoney
    subMethodNames_CpOrderId:(NSString*)varNames_argcpOrderId
  subMethodNames_ProductName:(NSString*)varNames_argProductName
  subMethodNames_ProductDesc:(NSString*)varNames_argdescription
       subMethodNames_RoleId:(NSString*)varNames_argroleId
     subMethodNames_RoleName:(NSString*)varNames_argroleName
    subMethodNames_RoleLevel:(NSString*)varNames_argroleLevel
     subMethodNames_ServerID:(NSString*)varNames_argserverId
   subMethodNames_ServerName:(NSString*)varNames_argserverName
         subMethodNames_Memo:(NSString*)varNames_argmemo {
    
    NSMutableDictionary *varNames_tmpDic = [NSMutableDictionary dictionaryWithCapacity:20];
    NSString *varNames_tmpusername = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@", methodNames_getStringu(), methodNames_getStrings(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe()];
    [varNames_tmpDic setValue:methodNames_readUserName() forKey:varNames_tmpusername];
    NSString *varNames_tmpuid = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringu(), methodNames_getStringi(), methodNames_getStringd()];
    [varNames_tmpDic setValue:methodNames_readUserID() forKey:varNames_tmpuid];
    NSString *varNames_tmpadvid = [NSString stringWithFormat:@"%@%@%@%@%@%@", methodNames_getStringa(), methodNames_getStringd(), methodNames_getStringv(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    [varNames_tmpDic setValue:methodNames_readAdvID() forKey:varNames_tmpadvid];
    NSString *varNames_tmpgid = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    [varNames_tmpDic setValue:methodNames_readGameID() forKey:varNames_tmpgid];
    NSString *varNames_tmpsubgid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringu(), methodNames_getStringb(), methodNames_getStringUnderLine(), methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    [varNames_tmpDic setValue:methodNames_readSubGameID() forKey:varNames_tmpsubgid];
    NSString *varNames_tmpplatformid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringp(), methodNames_getStringl(), methodNames_getStringa(), methodNames_getStringt(), methodNames_getStringf(), methodNames_getStringo(), methodNames_getStringr(), methodNames_getStringm(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    [varNames_tmpDic setValue:methodNames_readPlatformID() forKey:varNames_tmpplatformid];
    NSString *varNames_tmpchannelid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringc(), methodNames_getStringh(), methodNames_getStringa(), methodNames_getStringn(), methodNames_getStringn(), methodNames_getStringe(), methodNames_getStringl(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    [varNames_tmpDic setValue:methodNames_readChannelID() forKey:varNames_tmpchannelid];
    NSString *varNames_tmpgamever = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@", methodNames_getStringg(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr()];
    [varNames_tmpDic setValue:methodNames_readGameVersion() forKey:varNames_tmpgamever];
    NSString *varNames_tmpdevicecode = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringv(), methodNames_getStringi(), methodNames_getStringc(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringc(), methodNames_getStringo(), methodNames_getStringd(), methodNames_getStringe()];
    [varNames_tmpDic setValue:methodNames_getDeviceIDFA() forKey:varNames_tmpdevicecode];
    
    
    NSString *varNames_tmpcpserverid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringc(), methodNames_getStringp(), methodNames_getStringUnderLine(), methodNames_getStrings(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    [varNames_tmpDic setValue:varNames_argserverId forKey:varNames_tmpcpserverid];
    NSString *varNames_tmpservername = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe()];
    [varNames_tmpDic setValue:varNames_argserverName forKey:varNames_tmpservername];
    NSString *varNames_tmppaymoney = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@", methodNames_getStringp(), methodNames_getStringa(), methodNames_getStringy(), methodNames_getStringUnderLine(), methodNames_getStringm(), methodNames_getStringo(), methodNames_getStringn(), methodNames_getStringe(), methodNames_getStringy()];
    [varNames_tmpDic setValue:varNames_argmoney forKey:varNames_tmppaymoney];
    NSString *varNames_tmpproductname = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringp(), methodNames_getStringr(), methodNames_getStringo(), methodNames_getStringd(), methodNames_getStringu(), methodNames_getStringc(), methodNames_getStringt(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe()];
    [varNames_tmpDic setValue:varNames_argProductName forKey:varNames_tmpproductname];
    NSString *varNames_tmpgamegrade = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringg(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringg(), methodNames_getStringr(), methodNames_getStringa(), methodNames_getStringd(), methodNames_getStringe()];
    [varNames_tmpDic setValue:varNames_argroleLevel forKey:varNames_tmpgamegrade];
    NSString *varNames_tmproleid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStringr(), methodNames_getStringo(), methodNames_getStringl(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    [varNames_tmpDic setValue:varNames_argroleId forKey:varNames_tmproleid];
    NSString *varNames_tmprolename = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@", methodNames_getStringr(), methodNames_getStringo(), methodNames_getStringl(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe()];
    [varNames_tmpDic setValue:varNames_argroleName forKey:varNames_tmprolename];
    NSString *varNames_tmpcporderid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringc(), methodNames_getStringp(), methodNames_getStringUnderLine(), methodNames_getStringo(), methodNames_getStringr(), methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    [varNames_tmpDic setValue:varNames_argcpOrderId forKey:varNames_tmpcporderid];
    NSString *varNames_tmpdesc = [NSString stringWithFormat:@"%@%@%@%@", methodNames_getStringd(), methodNames_getStringe(), methodNames_getStrings(), methodNames_getStringc()];
    [varNames_tmpDic setValue:varNames_argdescription forKey:varNames_tmpdesc];
    NSString *varNames_tmpmemo = [NSString stringWithFormat:@"%@%@%@%@", methodNames_getStringm(), methodNames_getStringe(), methodNames_getStringm(), methodNames_getStringo()];
    [varNames_tmpDic setValue:varNames_argmemo forKey:varNames_tmpmemo];
    NSString *varNames_tmpproductid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@", methodNames_getStringp(), methodNames_getStringr(), methodNames_getStringo(), methodNames_getStringd(), methodNames_getStringu(), methodNames_getStringc(), methodNames_getStringt(), methodNames_getStringI(), methodNames_getStringd()];
    [varNames_tmpDic setValue:varNames_argproductId forKey:varNames_tmpproductid];
    [ClassNames_PGHubView methodNames_showIndicatorWithTitlte:[self.varNames_languageContent methodNames_getCommitBtnLoadingTip:varNames_purchaseViewEnum]];
    __weak typeof(self) weakSelf = self;
    __block NSString *varNames_tmpProductID = varNames_argproductId;
    __block NSString *varNames_tmpMoney = varNames_argmoney;
    [self.varNames_orderModel methodNames_fetchDataWithParameters:varNames_tmpDic];
    self.varNames_orderModel.varNames_fetchCompleteSuccess = ^(ClassNames_MemberOrderModel *varNames_argObject) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [ClassNames_PGHubView methodNames_hide];
            [weakSelf methodNames_payWithOrderModel:varNames_argObject subMethodNames_productid:varNames_tmpProductID subMethodNames_money:varNames_tmpMoney];
        });
    };
    self.varNames_orderModel.varNames_fetchCompleteFailure = ^(NSString *varNames_argmessage) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [ClassNames_PGHubView methodNames_hide];
            [ClassNames_PGHubView methodNames_showErrorMessage:varNames_argmessage];
        });
    };
    self.varNames_orderModel.varNames_fetchError = ^(NSError *varNames_argError) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [ClassNames_PGHubView methodNames_hide];
            [ClassNames_PGHubView methodNames_showErrorMessage:[weakSelf.varNames_languageContent methodNames_getFetErrorTip]];
        });
    };
    
    [self methodNames_startReplenishAction];
}

- (void)methodNames_payWithOrderModel:(ClassNames_MemberOrderModel *)varNames_argOrderModel
             subMethodNames_productid:(NSString *)varNames_argproductid
                 subMethodNames_money:(NSString *)varNames_argmoney {
    if ([varNames_argOrderModel.varNames_pay_type isEqualToString:@"OFF"]) {
        [[ClassNames_IAPPayManager sharedCenter]methodNames_startPayWithProductID:varNames_argproductid subMethodNames_money:varNames_argmoney subMethodNames_ordercode:varNames_argOrderModel.varNames_order_code subMethodNames_CompleteHandler:^(BOOL varNames_paySuccess) {
            methodNames_debugLog(@(varNames_paySuccess));
        }];
    } else {
        [ClassNames_RechargeView methodNames_showPayWebViewWithURL:varNames_argOrderModel.varNames_pay_url];
    }
}


#pragma mark ---------- 初始化成功数据处理
- (void)methodNames_dealWithSuccessInit:(ClassNames_GameInitialiseModel *)varNames_argGameInitModel {
    
    methodNames_saveLang(varNames_argGameInitModel.varNames_lang);
    methodNames_saveChannelID(varNames_argGameInitModel.varNames_channel_id);
    methodNames_saveProtocolSwitch(varNames_argGameInitModel.varNames_is_protocol);
    methodNames_saveProtocolURL(varNames_argGameInitModel.varNames_url);
    methodNames_saveswitch1Login(varNames_argGameInitModel.varNames_switch_1login);
    methodNames_saveAppleCheck(varNames_argGameInitModel.varNames_switch_appleCheck);
    methodNames_saveGameInitBindConfig(varNames_argGameInitModel.varNames_switch_bind);
    methodNames_saveBall(varNames_argGameInitModel.varNames_is_ball);
    
    [self methodNames_postInit:varNames_argGameInitModel];
    
}
#pragma mark ---------- 初始化成功失败发送的通知
- (void)methodNames_postInit:(ClassNames_GameInitialiseModel *)varNames_argGameInitModel {
    NSMutableDictionary *varNames_tmpDic = [NSMutableDictionary dictionaryWithCapacity:5];
    NSString *varNames_tmpresult = [NSString stringWithFormat:@"%@%@%@%@%@%@", methodNames_getStringr(), methodNames_getStringe(), methodNames_getStrings(), methodNames_getStringu(), methodNames_getStringl(), methodNames_getStringt()];
    NSString *varNames_tmpmsg = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringm(), methodNames_getStrings(), methodNames_getStringg()];
    NSString *varNames_tmpseturl = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringe(), methodNames_getStringt(), methodNames_getStringUnderLine(), methodNames_getStringu(), methodNames_getStringr(), methodNames_getStringl()];
    NSString *varNames_tmpformat = [NSString stringWithFormat:@"%@%@%@%@%@%@", methodNames_getStringf(), methodNames_getStringo(), methodNames_getStringr(), methodNames_getStringm(), methodNames_getStringa(), methodNames_getStringt()];
    NSString *varNames_tmpapplecheck = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringa(), methodNames_getStringp(), methodNames_getStringp(), methodNames_getStringl(), methodNames_getStringe(), methodNames_getStringC(), methodNames_getStringh(), methodNames_getStringe(), methodNames_getStringc(), methodNames_getStringk()];
    
    [varNames_tmpDic setValue:varNames_argGameInitModel.varNames_set_url forKey:varNames_tmpseturl];
    [varNames_tmpDic setValue:varNames_argGameInitModel.varNames_format forKey:varNames_tmpformat];
    [varNames_tmpDic setValue:methodNames_getStringOne() forKey:varNames_tmpresult];
    [varNames_tmpDic setValue:varNames_argGameInitModel.varNames_switch_appleCheck forKey:varNames_tmpapplecheck];
    [varNames_tmpDic setValue:@"initSuccess" forKey:varNames_tmpmsg];
    
    methodNames_postInitFinish(nil, varNames_tmpDic);
}

- (void)methodNames_initFinishPostNotiWithResult:(NSString *)varNames_argresult subMethodNames_msg:(NSString *)varNames_argmsg {
    NSMutableDictionary *varNames_tmpDic = [NSMutableDictionary dictionary];
    
    [varNames_tmpDic setValue:@"" forKey:@"set_url"];
    [varNames_tmpDic setValue:@"" forKey:@"format"];
    [varNames_tmpDic setValue:varNames_argresult forKey:@"result"];
    [varNames_tmpDic setValue:@"1" forKey:@"appleCheck"];
    [varNames_tmpDic setValue:varNames_argmsg forKey:@"msg"];
    methodNames_postInitFinish(nil, varNames_tmpDic);
}
#pragma mark ---------- 激活设备
- (void)methodNames_activateDeviceWithGid:(NSString *)varNames_arggid subMethodNames_subgid:(NSString *)varNames_argsubgid {
    
    if (!methodNames_readActivateDevice()) {
        [self methodNames_fetchActivateDeviceWithGid:varNames_arggid subMethodNames_subgid:varNames_argsubgid];
    } else {
        methodNames_debugLog(@"该设备已经激活了，不再激活设备");
    }
}

- (void)methodNames_fetchActivateDeviceWithGid:(NSString *)varNames_arggid subMethodNames_subgid:(NSString *)varNames_argsubgid {
    NSMutableDictionary *varNames_tmpDic = [NSMutableDictionary dictionaryWithCapacity:17];
    NSString *varNames_tmpgid = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpsubgid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringu(), methodNames_getStringb(), methodNames_getStringUnderLine(), methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpadvid = [NSString stringWithFormat:@"%@%@%@%@%@%@", methodNames_getStringa(), methodNames_getStringd(), methodNames_getStringv(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpchannelid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringc(), methodNames_getStringh(), methodNames_getStringa(), methodNames_getStringn(), methodNames_getStringn(), methodNames_getStringe(), methodNames_getStringl(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpplatformid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringp(), methodNames_getStringl(), methodNames_getStringa(), methodNames_getStringt(), methodNames_getStringf(), methodNames_getStringo(), methodNames_getStringr(), methodNames_getStringm(), methodNames_getStringUnderLine(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpdevicecode = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringv(), methodNames_getStringi(), methodNames_getStringc(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringc(), methodNames_getStringo(), methodNames_getStringd(), methodNames_getStringe()];
    NSString *varNames_tmpmac = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringm(), methodNames_getStringa(), methodNames_getStringc()];
    NSString *varNames_tmpgameversion = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@%@%@", methodNames_getStringg(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe(), methodNames_getStringUnderLine(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStrings(), methodNames_getStringi(), methodNames_getStringo(), methodNames_getStringn()];
    NSString *varNames_tmpmodeltype = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringm(), methodNames_getStringo(), methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringl(), methodNames_getStringUnderLine(), methodNames_getStringt(), methodNames_getStringy(), methodNames_getStringp(), methodNames_getStringe()];
    NSString *varNames_tmpmodelno = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@", methodNames_getStringm(), methodNames_getStringo(), methodNames_getStringd(), methodNames_getStringe(), methodNames_getStringl(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringo()];
    NSString *varNames_tmpresolution = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringr(), methodNames_getStringe(), methodNames_getStrings(), methodNames_getStringo(), methodNames_getStringl(), methodNames_getStringu(), methodNames_getStringt(), methodNames_getStringi(), methodNames_getStringo(), methodNames_getStringn()];
    NSString *varNames_tmposversion = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@%@", methodNames_getStringo(), methodNames_getStrings(), methodNames_getStringUnderLine(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStrings(), methodNames_getStringi(), methodNames_getStringo(), methodNames_getStringn()];
    NSString *varNames_tmpbrand = [NSString stringWithFormat:@"%@%@%@%@%@", methodNames_getStringb(), methodNames_getStringr(), methodNames_getStringa(), methodNames_getStringn(), methodNames_getStringd()];
    NSString *varNames_tmpnet = [NSString stringWithFormat:@"%@%@%@", methodNames_getStringn(), methodNames_getStringe(), methodNames_getStringt()];
    NSString *varNames_tmpother = [NSString stringWithFormat:@"%@%@%@%@%@", methodNames_getStringo(), methodNames_getStringt(), methodNames_getStringh(), methodNames_getStringe(), methodNames_getStringr()];
    NSString *varNames_tmpidfv = [NSString stringWithFormat:@"%@%@%@%@", methodNames_getStringi(), methodNames_getStringd(), methodNames_getStringf(), methodNames_getStringv()];
    NSString *varNames_tmpsdkver = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringd(), methodNames_getStringk(), methodNames_getStringUnderLine(), methodNames_getStringv(), methodNames_getStringe(), methodNames_getStringr()];
    
    [varNames_tmpDic setValue:varNames_arggid forKey:varNames_tmpgid];
    [varNames_tmpDic setValue:varNames_argsubgid forKey:varNames_tmpsubgid];
    [varNames_tmpDic setValue:methodNames_readAdvID() forKey:varNames_tmpadvid];
    [varNames_tmpDic setValue:methodNames_readChannelID() forKey:varNames_tmpchannelid];
    [varNames_tmpDic setValue:methodNames_readPlatformID() forKey:varNames_tmpplatformid];
    [varNames_tmpDic setValue:methodNames_getDeviceIDFA() forKey:varNames_tmpdevicecode];
    [varNames_tmpDic setValue:methodNames_getStringZero() forKey:varNames_tmpmac];
    [varNames_tmpDic setValue:methodNames_getProjectVersion() forKey:varNames_tmpgameversion];
    [varNames_tmpDic setValue:methodNames_getDeviceType() forKey:varNames_tmpmodeltype];
    [varNames_tmpDic setValue:methodNames_getDeviceType() forKey:varNames_tmpmodelno];
    [varNames_tmpDic setValue:methodNames_getDeviceResolution() forKey:varNames_tmpresolution];
    [varNames_tmpDic setValue:methodNames_getDeviceSystemVersion() forKey:varNames_tmposversion];
    [varNames_tmpDic setValue:methodNames_getDeviceBrand() forKey:varNames_tmpbrand];
    [varNames_tmpDic setValue:methodNames_getDeviceNetType() forKey:varNames_tmpnet];
    [varNames_tmpDic setValue:methodNames_getStringZero() forKey:varNames_tmpother];
    [varNames_tmpDic setValue:methodNames_getDeviceUUID() forKey:varNames_tmpidfv];
    [varNames_tmpDic setValue:methodNames_getSDKVersion() forKey:varNames_tmpsdkver];
    
    [self.varNames_activateModel methodNames_fetchDataWithParameters:varNames_tmpDic];
    self.varNames_activateModel.varNames_fetchCompleteSuccess = ^(ClassNames_ActivateModel *varNames_argObject) {
        methodNames_debugLog(varNames_argObject.varNames_msg);
        methodNames_saveActivateDevice();
    };
    self.varNames_activateModel.varNames_fetchCompleteFailure = ^(NSString *varNames_argmessage) {
        methodNames_debugLog(varNames_argmessage);
    };
}


#pragma mark ---------- 接收登录成功的通知
- (void)methodNames_loginNoti:(NSNotification *)noti {
    __weak typeof(self) weakSelf = self;
    dispatch_async(dispatch_get_main_queue(), ^{
        weakSelf.varNames_mainView = nil;
        NSMutableDictionary *varNames_tmpDic = [NSMutableDictionary dictionaryWithDictionary:[noti userInfo]];
        NSString *varNames_tmpresult = [NSString stringWithFormat:@"%@%@%@%@%@%@", methodNames_getStringr(), methodNames_getStringe(), methodNames_getStrings(), methodNames_getStringu(), methodNames_getStringl(), methodNames_getStringt()];
        NSString *varNames_tmpShowBall = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringh(), methodNames_getStringo(), methodNames_getStringw(), methodNames_getStringB(), methodNames_getStringa(), methodNames_getStringl(), methodNames_getStringl()];
        NSString *varNames_tmpResultValue = [varNames_tmpDic objectForKey:varNames_tmpresult];
        BOOL varNames_tmpShowBallValue = [[varNames_tmpDic objectForKey:varNames_tmpShowBall]boolValue];
        if ([varNames_tmpResultValue isEqualToString:methodNames_getStringOne()]) {
            if (varNames_tmpShowBallValue) {
                [weakSelf methodNames_showSuspensionBallView];
            }
        }
    });
}
#pragma mark ---------- 显示悬浮球
- (void)methodNames_showSuspensionBallView {
    __weak typeof(self) weakSelf = self;
    NSInteger varNames_showballduration = methodNames_getShowSuspensionBallDelayDuration();
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(varNames_showballduration * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
        [weakSelf methodNames_showSuspensionBall];
    });
}

- (void)methodNames_showSuspensionBall {
    __weak typeof(self) weakSelf = self;
    if (!self.varNames_suspensionBall || !self.varNames_suspensionBall.superview) {
        self.varNames_suspensionBall = [ClassNames_SuspensionBallButton methodNames_showSuspensionBall:varNames_showBallTypeLeft];
        self.varNames_suspensionBall.methodNames_clickBallMenu = ^(NSString *varNames_title) {
            if ([varNames_title isEqualToString:@"客服"]) {
                [weakSelf methodNames_showQQ];
            } else {
                [weakSelf methodNames_showWalkThrough];
            }
        };
    }
}

- (void)methodNames_showQQ {
    __weak typeof(self) weakSelf = self;
    [ClassNames_PGHubView methodNames_show];
    NSMutableDictionary *varNames_tmpPara = [NSMutableDictionary dictionaryWithCapacity:2];
    NSString *varNames_tmpsubgid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringu(), methodNames_getStringb(), methodNames_getStringUnderLine(), methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpusername = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@", methodNames_getStringu(), methodNames_getStrings(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe()];
    [varNames_tmpPara setValue:methodNames_readSubGameID() forKey:varNames_tmpsubgid];
    [varNames_tmpPara setValue:methodNames_readUserName() forKey:varNames_tmpusername];
    [self.varNames_qqserverModel methodNames_fetchDataWithParameters:varNames_tmpPara];
    self.varNames_qqserverModel.varNames_fetchCompleteSuccess = ^(ClassNames_QQServerModel *varNames_argObject) {
        
        NSLog(@"QQdata:%@", varNames_argObject.varNames_data);
        
        dispatch_async(dispatch_get_main_queue(), ^{
            methodNames_debugLog(varNames_argObject.varNames_url);
            [ClassNames_PGHubView methodNames_hide];
            [ClassNames_CustomServerView methodNames_showCustomServerViewWithContentJson:varNames_argObject.varNames_data];
        });
    };
    self.varNames_qqserverModel.varNames_fetchCompleteFailure = ^(NSString *varNames_argmessage) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [ClassNames_PGHubView methodNames_hide];
            [ClassNames_PGHubView methodNames_showErrorMessage:varNames_argmessage];
        });
    };
    self.varNames_qqserverModel.varNames_fetchError = ^(NSError *varNames_argError) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [ClassNames_PGHubView methodNames_hide];
            [ClassNames_PGHubView methodNames_showErrorMessage:[weakSelf.varNames_languageContent methodNames_getFetErrorTip]];
        });
    };
}

- (void)methodNames_showWalkThrough {
    __weak typeof(self) weakSelf = self;
    [ClassNames_PGHubView methodNames_show];
    NSMutableDictionary *varNames_tmpPara = [NSMutableDictionary dictionaryWithCapacity:2];
    NSString *varNames_tmpsubgid = [NSString stringWithFormat:@"%@%@%@%@%@%@%@", methodNames_getStrings(), methodNames_getStringu(), methodNames_getStringb(), methodNames_getStringUnderLine(), methodNames_getStringg(), methodNames_getStringi(), methodNames_getStringd()];
    NSString *varNames_tmpusername = [NSString stringWithFormat:@"%@%@%@%@%@%@%@%@%@", methodNames_getStringu(), methodNames_getStrings(), methodNames_getStringe(), methodNames_getStringr(), methodNames_getStringUnderLine(), methodNames_getStringn(), methodNames_getStringa(), methodNames_getStringm(), methodNames_getStringe()];
    [varNames_tmpPara setValue:methodNames_readSubGameID() forKey:varNames_tmpsubgid];
    [varNames_tmpPara setValue:methodNames_readUserName() forKey:varNames_tmpusername];
    [self.varNames_walkthroughModel methodNames_fetchDataWithParameters:varNames_tmpPara];
    self.varNames_walkthroughModel.varNames_fetchCompleteSuccess = ^(ClassNames_WalkThroughModel *varNames_argObject) {
        dispatch_async(dispatch_get_main_queue(), ^{
            methodNames_debugLog(varNames_argObject.varNames_url);
            [ClassNames_PGHubView methodNames_hide];
            NSLog(@"攻略:%@", varNames_argObject.varNames_data);
#pragma mark ---------- 此处需要完善攻略的内容
        });
    };
    self.varNames_walkthroughModel.varNames_fetchCompleteFailure = ^(NSString *varNames_argmessage) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [ClassNames_PGHubView methodNames_hide];
            [ClassNames_PGHubView methodNames_showErrorMessage:varNames_argmessage];
        });
    };
    self.varNames_walkthroughModel.varNames_fetchError = ^(NSError *varNames_argError) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [ClassNames_PGHubView methodNames_hide];
            [ClassNames_PGHubView methodNames_showErrorMessage:[weakSelf.varNames_languageContent methodNames_getFetErrorTip]];
        });
    };
}


#pragma mark ---------- 开启补单
- (void)methodNames_startReplenishAction {
    [[ClassNames_IAPReplenishmentManager shareCenter]methodNames_startReplenishOrderTimer];
}
#pragma mark ---------- 强制停止发起的补单申请
- (void)methodNames_stopReplenishAction {
    [[ClassNames_IAPReplenishmentManager shareCenter]methodNames_stopReplenishOrderFetch];
}


#pragma mark ---------- Getter
-(ClassNames_BaseLanguageContent *)varNames_languageContent {
    if (!_varNames_languageContent) {
        _varNames_languageContent = [[ClassNames_LanguageFactorManager methodNames_createTitleBaseFactor:methodNames_readLang()] methodNames_createContent];
    }
    return _varNames_languageContent;
}

-(ClassNames_MembeRoleModel *)varNames_uploadMemberRoleModel {
    if (!_varNames_uploadMemberRoleModel) {
        _varNames_uploadMemberRoleModel = (ClassNames_MembeRoleModel *)[ClassNames_ModelFactory methodNames_createModel:varNames_modelUpdateRole];
    }
    return _varNames_uploadMemberRoleModel;
}

-(ClassNames_UpdateUserLoginModel *)varNames_uploadLoginModel {
    if (!_varNames_uploadLoginModel) {
        _varNames_uploadLoginModel = (ClassNames_UpdateUserLoginModel *)[ClassNames_ModelFactory methodNames_createModel:varNames_modelUpdateLogin];
    }
    return _varNames_uploadLoginModel;
}

-(ClassNames_GameInitialiseModel *)varNames_gameInitModel {
    if (!_varNames_gameInitModel) {
        _varNames_gameInitModel = (ClassNames_GameInitialiseModel *)[ClassNames_ModelFactory methodNames_createModel:varNames_modelInit];
    }
    return _varNames_gameInitModel;
}

-(ClassNames_ActivateModel *)varNames_activateModel {
    if (!_varNames_activateModel) {
        _varNames_activateModel = (ClassNames_ActivateModel *)[ClassNames_ModelFactory methodNames_createModel:varNames_modelDevice];
    }
    return _varNames_activateModel;
}

-(ClassNames_QQServerModel *)varNames_qqserverModel {
    if (!_varNames_qqserverModel) {
        _varNames_qqserverModel = (ClassNames_QQServerModel *)[ClassNames_ModelFactory methodNames_createModel:varNames_modelQQServer];
    }
    return _varNames_qqserverModel;
}

-(ClassNames_WalkThroughModel *)varNames_walkthroughModel {
    if (!_varNames_walkthroughModel) {
        _varNames_walkthroughModel = (ClassNames_WalkThroughModel *)[ClassNames_ModelFactory methodNames_createModel:varNames_modelWalkThrough];
    }
    return _varNames_walkthroughModel;
}

-(ClassNames_MemberOrderModel *)varNames_orderModel {
    if (!_varNames_orderModel) {
        _varNames_orderModel = (ClassNames_MemberOrderModel *)[ClassNames_ModelFactory methodNames_createModel:varNames_modelOrder];
    }
    return _varNames_orderModel;
}
-(ClassNames_GameInitialiseModel *)varNames_beforeLoginInitModel {
    if (!_varNames_beforeLoginInitModel) {
        _varNames_beforeLoginInitModel = (ClassNames_GameInitialiseModel *)[ClassNames_ModelFactory methodNames_createModel:varNames_modelInit];
    }
    return _varNames_beforeLoginInitModel;
}
@end
