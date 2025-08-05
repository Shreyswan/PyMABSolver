sol = MABSolver(n=5, t=500, tf=200, eps=0.1, init_t=3, c=0.2)

avg_rew_list_expr, rewards = sol.exploration()
avg_rew_list_expl, rewards = sol.exploitation()
avg_rew_list_fege, rewards = sol.fixed_exploration_greedy_exploitation()
avg_rew_list_eps, rewards = sol.epsilon_greedy()
avg_rew_list_ucb, rewards = sol.ucb()

sol.plot_comparison(avg_rew_list_expr=avg_rew_list_expr, 
                    avg_rew_list_expl=avg_rew_list_expl, 
                    avg_rew_list_fege=avg_rew_list_fege, 
                    avg_rew_list_eps=avg_rew_list_eps, 
                    avg_rew_list_ucb=avg_rew_list_ucb)
