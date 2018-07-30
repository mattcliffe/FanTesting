clear all; 
clc

fname = 'AlphasenseData_26072018_3.csv';
data = importfile(fname);
dt = datetime(datenum(data.DateTime),'convertfrom','datenum');

window = 20;

pmr1_av1 = movmean(data.PMr1,[window 0]);
pmr2_av1  = movmean(data.PMr2,[window 0]);


figure(1)
clf()
subplot(311)
scatter(dt,data.PMr1,3,'k')
hold on 
scatter(dt,data.PMr2,3,'r')
hold on 
plot(dt,pmr1_av1,'k','linewidth',3)
hold on 
plot(dt,pmr2_av1,'r','linewidth',3)

ylabel('PMr [ug/m3]')
grid('on')

subplot(312)
plot(dt,data.SFR1,'k')
hold on 
plot(dt,data.SFR2,'r')
ylabel('SFR [ml/s]')
grid('on')

subplot(313)
plot(dt,data.FanVoltage)
ylabel('Fan Voltage [V]')
grid('on')

print([fname(1:25),'movaverage.png'],'-dpng')

