clear
clc
close all

count = readtable('Data\for_intersection_plots\dacs_count_all.csv');
log_count = log10(count.Var1);
cnt_dacs = readtable('Data\for_intersection_plots\cnt_dacs_threshold.csv');

positive_frac = readtable('Data\for_intersection_plots\positive_frac_dacs.csv');
frac_dacs = readtable('Data\for_intersection_plots\frac_dacs_threshold.csv');


figure
xlim([-0.03 1.43]);
yyaxis left
P = plot(cnt_dacs.Var1,log_count,LineWidth=2,Color=[0.2 0.35 0.9]);
xlabel('DACS threshold','FontSize',11.5)
ylabel('Number of combinations','FontSize',11.5)
yticks([2 3 4 5 6 7])
yticklabels({'1e+02', '1e+03', '1e+04', '1e+05', '1e+06', '1e+07'})

yyaxis right
PP = plot(frac_dacs.Var1,positive_frac.Var1,LineWidth=1.79,...
    Color=[0.65 0.15 0.75], LineStyle="--");
line([0.534 0.534], [0 0.814], 'Color', 'k', 'LineStyle', ':', LineWidth=1.79);
ylabel("Fraction of drug-pairs with positive Kendall \tau",...
    'FontSize',11.5)
ylim([0.535 1.02]);
ax = gca;
ax.YAxis(1).Color = '[0.2 0.35 0.9]';
ax.YAxis(2).Color = '[0.65 0.15 0.75]';
ax.FontSize = 12; 
ax.FontName = 'Adobe Devanagari';
legend('Number of combinations','Fraction of positive correlations',...
    'FontSize',11.5)
fontname(gcf,"Bitstream Vera Sans")
